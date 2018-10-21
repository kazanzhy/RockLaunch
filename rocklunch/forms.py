from wtforms import Form, StringField, DateField, IntegerField


class LaunchSearchForm(Form):
    startdate = StringField()
    enddate = StringField()
    limit = IntegerField()
