<template>
<section class="hero is-fullheight is-info">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Submit Feedback</p>
        <hr />
        <p class="subtitle">Please fill out this form and and the upcoming survey to let me know about your opinions</p>

        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_feedback()" v-if="feedback_mode">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>
              <div class="field">
                <div class="control">
                  <textarea
                      class="textarea is-medium"
                      placeholder="Please let me know what you think about this project. Were there any problems? Was there a mistake along the way?"
                      v-model="opinions"
                  ></textarea>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <textarea
                      class="textarea is-medium"
                      placeholder="Is there something that could've been done differently?"
                      v-model="suggestions"
                  ></textarea>
                </div>
              </div>

              <div v-if="error_message">
                <p class="is-danger help">
                  {{ error_message }}
                </p>
                <p class="has-text-info help">
                  {{ warning_message }}
                </p>
              </div>
              <br />

              <button class="button is-info">Submit Feedback</button>
            </form>
            <form class="box" @submit.prevent="submit_answers()" v-if="survey_mode">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>

              <div class="field" v-for="(question, index) in questions" :key="index">
                <div class="control">
                  <div class="box">
                    <div>
                      <h4 class="title is-4 has-text-black">
                        {{ question.id }}. {{ question.questions }}
                      </h4>
                    </div>
                    <div>
                       <label class="radio" v-for="(ans_choice, index) in question.ans_choices" :key="index">
                        <input v-model="answer_form.answers[question.id]" type="radio" :name="question.id" v-bind:value="ans_choice[0]">
                        {{ ans_choice[1] }}
                      </label>
                    </div>
                  </div>
                  <br>
                </div>
              </div>

              <div v-if="error_message">
                <p class="is-danger help">
                  {{ error_message }}
                </p>
                <p class="has-text-info help">
                  {{ warning_message }}
                </p>
              </div>
              <br />

              <button class="button is-info">Submit Answers</button>
            </form>
            <div class="box" v-if="user_feedback_mode">
              <div>
                <h4 class="title is-4 has-text-black">
                  <u>Opinions:</u>
                </h4>
                <p>{{ opinions }}</p>
              </div>
              <br>
              <div>
                <h4 class="title is-4 has-text-black">
                  <u>Suggestion:</u>
                </h4>
                <p>{{ suggestions }}</p>
              </div>
              <br>
              <div>
                  <h4 class="title is-4 has-text-black">
                    <u>Q&A</u>
                  </h4>
                 <div v-for="(a,q, index) in user_answers" :key="index">
                  <strong>{{q}}</strong>: {{ a }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { mapState } from 'vuex';
import {toast} from "bulma-toast";

export default{
  name:'Feedback',
  data(){
    return{
      opinions: null,
      suggestions: null,
      error_message: null,
      feedback_mode: true, // initial mode where they submit the suggestions and opinions
      survey_mode: false, // After submitting the suggestions and opinions
      user_feedback_mode: false, // Will allow us to see the user feedback
      feedback_id: null, // We are going to set this feedback_id so we could just submit the answers in this Vue view.
      questions: [],
      answer_form: {
        answers: []
      },
      user_answers: {},
    }
  },
  computed:{
    ...mapState(['user_id'])
  },
  methods:{
    user_feedback(){
      axios.get(`feedbacks/get_feedback/${this.feedback_id}/`).then((response)=>{
        // So we don't need to set opinions and suggestions because we already have them in our data
        // Once we post our feedback we want to view it so let's go ahead and activate feedback_mode
        this.survey_mode = !this.survey_mode
        this.user_feedback_mode = !this.user_feedback_mode
        this.user_answers = response.data.answers
      })
    },
    submit_feedback(){
      if(this.opinions !== null && this.suggestions !== null){
        let data = {
          user: this.user_id,
          opinions: this.opinions,
          suggestions: this.suggestions
        }
        axios.post('feedbacks/add_feedback/',data).then((response)=>{
          this.feedback_id = response.data.id   // This way once this feedback is created we could immediately add ans
          this.feedback_mode = !this.feedback_mode
          this.survey_mode = !this.survey_mode
        })
      }else{
        this.error_message = "Please fill in the blanks."
      }
    },
    submit_answers(){
      let data = []
      for(let ans_form in this.answer_form.answers){
        let data_format = {
          feedback: this.feedback_id,
          question: ans_form,
          answer: this.answer_form.answers[ans_form]
        }
        data.push(data_format)
      }

      axios.post('feedbacks/add_feedback_answers/', data).then(()=>{
        this.user_feedback()  // To update user_answers to display them and then change the mode
        toast({
          message: "Your feedback was submitted thank you :)",
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 2000, // milliseconds
          position: "bottom-right",
        });
      })
    }
  },
  created(){
    axios.get('feedbacks/questions/').then(response=>{
      this.questions = response.data  // note that each question comes with their ans_choices
    })
  }
}
</script>