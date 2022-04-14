<template>
  <div>
    <div class="field has-text-centered">
        <input
          id="adminSwitch"
          type="checkbox"
          name="adminSwitch"
          class="switch is-medium is-outlined is-danger"
          checked="checked"
          v-model="add_question_mode"
        />
        <label for="adminSwitch">Add Question</label>
    </div>
    <section class="section is-small" v-if="!add_question_mode">
      <div class="container">
        <div class="box has-text-centered has-background-info">
          <h2 class="title is-2 has-text-black">
            <u>
              <i>All Current Questions</i>
            </u>
          </h2>
          <ul>
            <li v-for="(question, index) in current_questions" :key="index">
              <h3 class="title is-3 has-text-white">
                <span>
                  {{ question.id }}. <strong>{{ question.questions }}</strong>
                </span>
                <span>
                  <button class="button is-outlined is-danger is-small ml-2"
                          @click="start_remove_question(index)">
                    <span class="icon is-small">
                      <i class="fas fa-times"></i>
                    </span>
                  </button>
                </span>

              </h3>
            </li>
          </ul>
        </div>
      </div>
    </section>
    <section class="section is-small" v-else>
      <div class="container">
        <div class="box has-text-centered has-background-primary">
          <h2 class="title is-2 has-text-black">
            <u>
              <i>Add Questions</i>
            </u>
          </h2>
          <div class="container">
            <div class="box has-text-centered">
              <div class="columns">
                <div class="column" id="added_question">
                  <div class="content">
                    <h3 class="title is-3">Your Added Questions Here: </h3>
                    <ul>
                      <li v-for="(added_question, index) in added_questions" :key="index">
                        <span>
                          {{index+1}}. {{added_question.questions}}
                        </span>
                        <span>
                          <button class="button is-outlined is-danger is-small ml-2" @click="remove_question(index)">
                             <span class="icon is-small">
                               <i class="fas fa-times"></i>
                             </span>
                          </button>
                        </span>

                      </li>

                    </ul><br>
                    <button class="button is-outlined is-primary"
                            v-if="added_questions.length !== 0"
                            @click="submit_questions()">
                      Submit Questions
                    </button>
                  </div>
                </div>
                <div class="column" id="add_question">
                  <h3 class="title is-3">Add Your Questions Here: </h3>
                  <div class="control">
                    <input class="input" type="text" v-model=added_question @keydown.enter="add_question()">
                  </div> <br>
                  <div>
                    <button class="button is-outlined is-primary" @click="add_question()">
                      Add Question
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Remove question Modal -->
    <div class="modal" :class="{'is-active': confirm_remove_question}">
      <div class="modal-background"></div>
      <div class="modal-content">
        <!-- Any other Bulma elements you want -->
        <div class="box has-text-centered">
          <div class="content">
            <h2 class="title is-2"> Removing: {{ removed_question.questions }}</h2>
          </div>
          <div>
            <button class="button is-outlined is-danger" @click="remove_confirmed_question(removed_question)">
              Confirm Removing: {{ removed_question.questions }}
            </button>
          </div>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close"
              @click="confirm_remove_question = !confirm_remove_question">
      </button>
    </div>

  </div>
</template>

<script>
import axios from "axios"
import Cookies from 'cookies-js'
import { toast } from 'bulma-toast'

export default{
  name: "QuestionControl",
  data(){
    return{
      view_question_mode: true,
      current_questions: [],
      add_question_mode: false,
      added_question: '',
      added_questions: [],
      removed_question: '',
      confirm_remove_question: false,
    }
  },
  methods:{
    start_remove_question(question){
      this.removed_question = this.current_questions[question]
      this.confirm_remove_question = !this.confirm_remove_question
    },
    remove_confirmed_question(question_obj){
      let config = {
        headers: {Authorization: `Bearer ${Cookies('accessToken')}`}
      }
      axios.delete(`admin_panel/feedbacks/remove_questions/${question_obj.id}/`, config).then((response)=>{
        this.confirm_remove_question = !this.confirm_remove_question
        toast({
              message: response.data.success,
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 6000, // milliseconds
              position: "bottom-right",
            });
      })
    },
    add_question(){
      let question_format = {
        questions: this.added_question
      }
      this.added_questions.push(question_format)
      this.added_question = ''
    },
    remove_question(question){
      this.added_questions.splice(question, 1)
    },
    submit_questions(){
      let config = {
        headers: {Authorization: `Bearer ${Cookies('accessToken')}`}
      }
      axios.post('admin_panel/feedbacks/add_questions/', this.added_questions, config).then((response)=>{
        console.log(response.data)
      })
    }
  },
  created() {
    axios.get('feedbacks/questions/').then((response)=>{
      // once we get all of the questions now lets get all the feedbacks
      this.current_questions = response.data
    })
  }
}
</script>

<style scoped>
li{
  list-style-type:none;
}
</style>