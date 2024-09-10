from school.models.app_settings_model import AppSettingModel
from school.models.school_model import SchoolModel


def get_element(request):
    app_setting = AppSettingModel.objects.first()
    school = SchoolModel.objects.first()

    context = {
        'app_setting': app_setting,
        'school': school,
    }

    return context