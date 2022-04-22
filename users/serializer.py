from rest_framework import serializers
from .models import Profile


# for ProfileSerializer we need their username so lets create custom field using SerializerMethodField
class ProfileSerializer(serializers.ModelSerializer):
    # creating the SerializerMethodField and grabbing value from function called get_username
    # REMOVED: trailing fields for easy index display on front end
    username = serializers.SerializerMethodField('get_username')
    feedback = serializers.SerializerMethodField('get_feedback')
    is_staff = serializers.SerializerMethodField('get_is_staff')

    def get_username(self, profile):
        # Profile getting the instance we can use to retrieve the username
        username = profile.user.username
        return username

    def get_feedback(self, profile):
        # We are going to return feedback which could be null so
        if profile.feedback_set.first():
            feedback = profile.feedback_set.first()
            answers = {ans.question.questions: ans.get_written_ans() for ans in feedback.feedbackanswers_set.all()}
            feedback_detail = {
                'opinions': feedback.opinions,
                'suggestions': feedback.suggestions,
                'answers': answers
            }
            return feedback_detail
        return None

    def get_is_staff(self, profile):
        return profile.user.is_staff

    class Meta:
        # Make sure you dont have , after Profile because ERROR: restframework 'tuple' object has no attribute '_meta'
        model = Profile
        fields = (
            'username',
            'is_staff',
            'date_joined',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'city',
            'country',
            'state',
            'zip_code',
            'feedback'
        )