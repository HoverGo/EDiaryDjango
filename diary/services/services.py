from ..models import DiaryRecord



def save_form(request, form):
    user = request.user
    name = form.data["name"]
    text = form.data["text"]

    instance = DiaryRecord(user=user, name=name, text=text)

    instance.save()


def get_diary_record(request, id):
    user = request.user

    instance = DiaryRecord.objects.get(id=id, user=user)

    return instance

def delete_record(request, id):
    user = request.user
    instance = DiaryRecord.objects.get(id=id, user=user)
    instance.delete()