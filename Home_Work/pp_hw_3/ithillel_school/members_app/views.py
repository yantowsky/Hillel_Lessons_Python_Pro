from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm


def member_list(request):
    members = Member.objects.select_related('course')
    return render(request, 'members_app/member_list.html', {'members': members})


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()

    return render(request, 'members_app/create_member.html', {'form': form})
