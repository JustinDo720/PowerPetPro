from rest_framework import serializers
from .models import Category, Product, MessageBox, MissionStatement, MissionDetails, MissionStatementTopics, Feedback, \
    FeedBackAnswers, FeedBackQuestions
from users.models import CustomUser, Profile
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
        )


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')
    limited_description = serializers.SerializerMethodField('get_limited_description')

    def get_category_name(self, product):
        category = Category.objects.get(id=product.category.id)
        return category.name

    def get_limited_description(self, product):
        if product.description:
            limited_description = product.description[:125]  # 50 characters
            return limited_description
        else:
            return ''

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'category_name',
            'image',
            'name',
            'description',
            'limited_description',
            'price',
            'date_added',
            # These are for the images
            'get_absolute_url',
            'get_image',
            'get_image_name',
            'get_thumbnail',
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


# Custom Register Serializer
class MyUserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password', 're_password')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['user_id'] = self.user.id  # We are going to use this for uuid
        data['is_staff'] = self.user.is_staff

        return data


class MessageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBox
        fields = (
            'id',
            'msg',
        )


class MissionStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionStatement
        fields = (
            'main_statement',
        )


class MissionStatementTopicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MissionStatementTopics
        fields = (
            'id',
            'slug',
            'topic',
        )


class MissionDetailsSerializer(serializers.ModelSerializer):
    mission_topic_name = serializers.SerializerMethodField('get_mission_topic_name')

    def get_mission_topic_name(self, detail):
        return detail.mission_topic.topic

    class Meta:
        model = MissionDetails
        fields = (
            'mission_topic', # Here we are going to get the id number that corresponds to our topic
            'mission_topic_name', # We want to get the name of our topic
            'mission_topic_details',
            'date_added',
        )


class FeedbackQuestionsSerializer(serializers.ModelSerializer):
    ans_choices = serializers.SerializerMethodField('get_ans_choices')

    def get_ans_choices(self, feedback_ans):
        return feedback_ans.get_answer_choices()

    class Meta:
        model = FeedBackQuestions
        fields = (
            'id',
            'questions',
            'ans_choices'
        )


class FeedbackAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBackAnswers
        fields = (
            'feedback',
            'question',
            'answer',
        )


class FeedbackSerializer(serializers.ModelSerializer):
    total_score = serializers.SerializerMethodField('get_total_score')
    answers = serializers.SerializerMethodField('get_answers')
    username = serializers.SerializerMethodField('get_username')
    grading_rule = serializers.SerializerMethodField('get_grading_rule')

    def get_total_score(self, feedback):
        ans_set = feedback.feedbackanswers_set.all()
        # answers = {ans.question.questions: ans.get_written_ans() for ans in feedback.feedbackanswers_set.all()}
        answers = {ans.question.questions: {'ans': ans.get_written_ans(), 'score': ans.get_score()} for ans in ans_set}
        total_score = 0
        scores = [a["score"] for (q, a) in answers.items()]
        for score in scores:
            total_score += score

        return total_score

    def get_answers(self, feedback):
        ans_set = feedback.feedbackanswers_set.all()
        answers = {ans.question.questions: ans.get_written_ans() for ans in ans_set}
        return answers

    def get_username(self, feedback):
        return feedback.user.username

    def get_grading_rule(self, feedback):
        return feedback.get_grading_rule()

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'username',
            'opinions',
            'suggestions',
            'date_submitted',
            'answers',
            'total_score',
            'grading_rule',
        )