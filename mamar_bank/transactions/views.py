from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TransactionsModel
from .forms import DepositeForm,WithdrawForm,LoanRequestForm
from .constrant import DEPOSIT,WITHDRAWAL,LOAN,LOAN_PAID
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.views import View
from django.urls import reverse_lazy
# Create your views here.

# ei view ke inherit kore amra deposite,withdraw,loan request er kaj korbo
class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transactions/transaction_form.html'
    model = TransactionsModel
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs.update({

            'account' : self.request.user.account,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        return context

class DepositeMoneyView(TransactionCreateMixin):
    form_class = DepositeForm
    title = 'Deposite'
    
    def get_initial(self):
        initial = {'transactions_type' : DEPOSIT}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        
        account = self.request.user.account
        
        account.balance += amount
        
        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request,f'{amount} $ was deposited to your account successfully')
        return super().form_valid(form)

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw'

    def get_initial(self):
        initial = {'transactions_type': WITHDRAWAL}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        
        account = self.request.user.account
        account.balance -= amount
        account.save(
            update_fields = ['balance']
        )
        messages.success(self.request,f'Successfully withdrawn {amount}$ from your account')
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transactions_type':LOAN}
        return initial

    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')

        current_loan_count = TransactionsModel.objects.filter(account = self.request.user.account,transactions_type = LOAN,loan_approve=True).count()

        if current_loan_count >=3:
            return HttpResponse('You have crossed your limits')
        
        messages.success(self.request,f'Loan request for amount {amount}$ sent to admin successfully')
        return super().form_valid(form)
    


class TransactionReportView(LoginRequiredMixin,ListView):
    template_name = 'transactions/transaction_report.html'
    model = TransactionsModel
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str,"%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str,"%Y-%m-%d").date()

            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)

            self.balance = TransactionsModel.objects.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
        
        return queryset.distinct() # unique queryset hote hobe
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })
        return context

class PayLoanView(LoginRequiredMixin,View):
    def get(self,request,loan_id):
        loan = get_object_or_404(TransactionsModel,id=loan_id)

        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance :
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.transactions_type = LOAN_PAID
                loan.save()
                return redirect('loan_list')
            else:
                messages.error(self.request,f'Loan amount is greater than available balance')
                return redirect('loan_list')



class LoanListView(LoginRequiredMixin,ListView):
    model = TransactionsModel
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'

    def get_queryset(self) -> QuerySet[Any]:
        user_account = self.request.user.account
        queryset = TransactionsModel.objects.filter(account = user_account,transactions_type=LOAN)
        return queryset