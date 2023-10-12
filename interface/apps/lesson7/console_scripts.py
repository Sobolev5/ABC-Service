import sys
from simple_print import sprint
from lesson7.models import Group, GroupUser
from django.db.models import F
from django.db.models import Q
from django.db.models import Max
from django.db.models import Count


def fill_database():
    # python run.py lesson7.console_scripts "fill_database()" 

    # Очистим
    Group.objects.all().delete()
    GroupUser.objects.all().delete()

    for name in ["Guests", "Developers", "Maintainers"]:    
        if name in Group.objects.all().values_list("name", flat=True):
            continue
        group = Group()
        group.name = name
        group.save()
        sprint(group.id)

    names = ["Ivan", "Petr", "Vasya"]
    for index, group in enumerate(Group.objects.all()):
        if names[index] in GroupUser.objects.all().values_list("name", flat=True):
            continue        
        group_user = GroupUser()
        group_user.name = names[index]
        group_user.group = group
        group_user.save()

        group.members_count = 1
        group.verified_members_count = 1   
        group.save()
        sprint(group_user.id) 


def basic_operations():
    # python run.py lesson7.console_scripts "basic_operations()" 

    # возьмем запись
    group = Group.objects.get(name="Guests")   

    # посмотрим PK/ID
    sprint(group.pk)
    sprint(group.id)

    # посмотрим имя
    sprint(group.name)

    # Исправим число участников
    group.members_count = 5
    group.verified_members_count = 5
    group.save()

    # возьмем все записи
    groups = Group.objects.all()
    groups = groups.filter(id=2) # lazy
    sprint(groups)

    # возьмем первые две 
    groups = Group.objects.all()[:2]
    sprint(groups)

    # отфильтруем
    groups = Group.objects.filter(name="Guests")
    groups = Group.objects.filter(name__icontains="sts")
    
    sprint(groups)

    # посмотрим выборку
    sprint(groups.query)    


def related_operations():
    # python run.py lesson7.console_scripts "related_operations()" 

    # возьмем запись
    group = Group.objects.get(name="Guests")   

    # посмотрим участников
    sprint(group.groupuser_set.all())

    # возьмем участника
    group_user = GroupUser.objects.first()

    # посмотрим его группу
    sprint(group_user.group)

    # можно посмотреть количество участников
    sprint(group_user.group.members_count)

    for group_user in GroupUser.objects.filter(group__name="Developers"):
        sprint(group_user)

    for group in Group.objects.filter(groupuser__name="Vasya"):
        sprint(group)

def filters_and_complex_lookups():
    # python run.py lesson7.console_scripts "filters_and_complex_lookups()" 

    # возьмем запись
    group = Group.objects.get(name="Guests")   

    # посмотрим ID
    sprint(group.id)

    # посмотрим имя
    sprint(group.name)

    # Исправим число участников
    group.members_count = 7
    group.save()

    # Отфильтруем группы где количество участников всего больше чем количество верифицированных участников 
    groups = Group.objects.filter(members_count__gt=F('verified_members_count'))  
    sprint(groups)

    # Выберем группы которые начинаются с Dev или с G
    groups = Group.objects.filter(Q(name__startswith='Dev') | Q(name__startswith='G'))
    sprint(groups)
    sprint(groups.query)

    # Максимальное количество участников (агрегация - сразу вычислить)
    max_members_count = Group.objects.all().aggregate(Max('members_count'))
    print(max_members_count)

    # Сумма полей members_count и verified_members_count  (аннотация - "добавить" вычисляемое поле)
    for group in Group.objects.annotate(sum_members_and_verified_members=F('members_count') + F('verified_members_count')):
        print(group.sum_members_and_verified_members)