<template>
  <section class="hero is-fullheight ">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Category</p>
        <hr />
        <p class="subtitle">Please Enter the follow information below to add a Category</p>

        <div class="columns is-centered">
          <div class="column is-5" v-if="show_added_category">
            <div class="box">
              <h1 class="title is-2">
                Category Added: {{ saved_category_name  }}
              </h1>
            </div>
          </div>
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_category()">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>
              <div class="field">
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Category Name"
                    v-model="category_name"
                  />
              </div>
              <button class="button is-success">Submit Category Name</button>
              <div>
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast';
import { mapState } from 'vuex';

export default{
  name:'AdminCategory',
  data(){
    return{
      category_name: null,
      show_added_category: false,
      error_message : null,
      saved_category_name: ''
    }
  },
  computed:{
    ...mapState(['accessToken']),
  },
  methods:{
    submit_category(){
        if(this.category_name){
          axios.post('admin_panel/post_category/',{
          name: this.category_name
        },{headers: {Authorization: `Bearer ${this.accessToken}`}}).then((response)=>{
          this.saved_category_name = response.data.name
          this.show_added_category = true
          toast({
            message: `${this.category_name} was added to Category list`,
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 6000, // milliseconds
            position: "bottom-right",
          })
          this.category_name = ''
        }).catch(err=>{
          console.log(err.response.data)
          this.error_message = err.response.data.name[0]
        })
      }else{
          this.error_message = 'Please fill out the form'
        }


    },
  }
}
</script>