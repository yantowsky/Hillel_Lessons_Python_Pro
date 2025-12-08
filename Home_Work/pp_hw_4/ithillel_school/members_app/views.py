from django.shortcuts import render, redirect
from members_app.models import Member
from .forms import MemberForm
from members_app.signals import course_member_synced


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


def attach_member_to_course(request, member_id):
    member = Member.objects.get(id=member_id)
    member.save()  # нормальний виклик

    # додатково — кастомний
    course_member_synced.send(sender=Member, instance=member)

    return HttpResponse("OK")
