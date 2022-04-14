<template>
  <div>
    <div class="has-text-centered">
      <h1 class="title is-1">
        <u>
          <i>
            User Feedbacks
          </i>
        </u>
      </h1>
      <button class="button is-light is-primary" @click="view_grading_guide= !view_grading_guide">
        View Grading Rule
      </button>
    </div>
    <section class="section is-small">
      <div class="container">
        <div class="box" v-for="(feedback, index) in all_feedbacks" :key="index">
          <div class="has-text-centered">
            <h3 class="title is-3">
              <i>
                {{ feedback.username }}'s Feedback
              </i>
            </h3><br>
          </div>
          <div class="columns">
            <div class="column">
              <div class="box has-background-info">
                <div class="tile is-ancestor">
                  <div class="tile is-vertical">
                    <div class="tile">
                      <div class="tile is-parent is-vertical">
                          <div class="box">
                            <div class="content">
                              <h4 class="title is-4">Opinions:</h4>
                              <p>
                                "{{ feedback.opinions }}"
                              </p>
                            </div>
                          </div>
                      </div>
                      <div class="tile is-parent is-vertical">
                          <div class="box">
                            <div class="content">
                              <h4 class="title is-4">Suggestion:</h4>
                              <p>
                                "{{ feedback.suggestions }}"
                              </p>
                            </div>
                          </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="column">
              <div class="box has-background-link">
                <div class="box">
                  <div class="content">
                    <h4 class="title is-4">Question&Answer:</h4>
                    <ul>
                      <li v-for="(answer, question, index) in feedback.answers" :key="index">
                        <strong><u>{{ question }}</u></strong> {{ answer }}
                      </li>
                    </ul>
                    <h5 class="title is-5"> Total Score: {{ feedback.total_score }}</h5>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <nav class="pagination is-medium" role="navigation" aria-label="pagination">
          <a class="pagination-previous" v-if="previous_page" @click="get_info(previous_page)">Previous</a>
          <a class="pagination-next" v-if="next_page" @click="get_info(next_page)">Next</a>
        </nav>
      </div>
    </section>

    <!-- grading guide modal -->
    <div class="modal" :class="{'is-active': view_grading_guide}">
      <div class="modal-background"></div>
      <div class="modal-content">
        <!-- Any other Bulma elements you want -->
        <div class="box has-text-centered">
          <h3 class="title is-3">Grading Rule</h3>
          <ul>
            <li>
              Min Grade: 0
            </li>
            <li v-for="(grading, key) in grading_rule" :key="key">
              Score: <u>{{ grading[0] }}</u> for <strong>"{{ grading[1] }}"</strong>
            </li>
            <li>
              Max Grade: {{ maxScore }}
            </li>
          </ul>
        </div>
      </div>
      <button class="modal-close is-large" aria-label="close" @click="view_grading_guide= !view_grading_guide"></button>
    </div>
  </div>
</template>

<script>

import Cookies from "cookies-js";
import axios from "axios";

export default{
  name: "AllFeedbacks",
  data(){
    return{
      all_feedbacks: [],
      previous_page: '',
      next_page: '',
      view_grading_guide: false,
      grading_rule: [],
    }
  },
  computed:{
    maxScore(){
      let max_grade = 0
      for(let grading in this.grading_rule){
        max_grade += this.grading_rule[grading][0]
      }
      return max_grade
    }
  },
  methods:{
    get_info(api_url){
      let config = {
        headers: { Authorization: `Bearer ${Cookies('accessToken')}`}
      }
      axios.get(api_url, config).then((response)=>{
        this.all_feedbacks = response.data.results
        this.grading_rule = response.data.results[0]['grading_rule'] // Grading rule is on all of the feedbacks

        if(response.data.next){
          this.next_page = response.data.next
        } else {
          this.next_page = ''
        }

        if(response.data.previous){
          this.previous_page = response.data.previous
        } else {
          this.previous_page = ''
        }
      })
    },
  },
  created(){
    let api_url ='admin_panel/feedbacks/'
    this.get_info(api_url)
  }
}
</script>

<style scoped>
li{
  list-style-type: none;
}
</style>