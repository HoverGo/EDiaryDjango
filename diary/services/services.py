from ..models import DiaryRecord



def save_form(request, form):
    user = request.user
    name = form.data["name"]
    text = form.data["text"]

    instance = DiaryRecord(user=user, name=name, text=text)

    instance.save()