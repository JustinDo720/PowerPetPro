<template>
<section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Messages</p>
        <hr />
        <p class="subtitle">Viewing all Messages</p>

        <div class="columns is-centered">
          <div class="column is-5">
             <div class="box">
                 <div class="box" v-for="(message, index) in messageboxes" :key="index">
                   <span>
                      {{index + 1}}.  {{ message.msg }}&nbsp;
                   </span>
                   <span>
                     <button class="button is-warning is-small" @click="edit_message_activation(message)">
                      <span class="icon is-small">
                        <i class="fas fa-pencil-alt"></i>
                      </span>
                      <span>Edit</span>
                    </button>&nbsp;
                   </span>
                   <span>
                     <button class="button is-danger is-small" @click="delete_message_activation(message)">
                      <span>Delete</span>
                      <span class="icon is-small">
                        <i class="fas fa-times"></i>
                      </span>
                    </button>
                   </span>
                </div>
               <nav class="pagination" role="navigation" aria-label="pagination">
                  <button class="pagination-previous is-disabled"
                          title="This is the first page"
                          @click="change_messagebox(previous_url)">
                    Previous
                  </button>
                  <button class="pagination-next" @click="change_messagebox(next_url)">
                    Next page
                  </button>

                </nav>
             </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="modal is-centered" :class="{'is-active':activate_edit_modal, 'is-clipped':activate_edit_modal}">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Edit Message</p>
        <button class="delete" aria-label="close" @click="activate_edit_modal=false"></button>
      </header>
      <section class="modal-card-body">
        <div class="box">
          Current Message: "{{ chosen_message }}"
        </div>
        <textarea class="textarea" v-model="chosen_message"></textarea>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-success" @click="edit_message()">Save changes</button>
        <button class="button" @click="activate_edit_modal=false">Cancel</button>
      </footer>
    </div>
  </div>

  <div class="modal is-centered" :class="{'is-active':activate_delete_modal, 'is-clipped':activate_delete_modal}">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm Delete Message</p>
        <button class="delete" aria-label="close" @click="activate_delete_modal=false"></button>
      </header>
      <section class="modal-card-body">
        <div class="box">
          Current Message: "{{ chosen_message }}"
        </div>
      </section>
      <footer class="modal-card-foot is-centered">
        <button class="button is-danger" @click="delete_message()">Delete Message</button>
        <button class="button" @click="activate_delete_modal=false">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import { toast } from 'bulma-toast'

export default{
  name: 'ViewAllMessages',
  computed:{
    ...mapState(['messageboxes', 'next_url', 'previous_url', 'accessToken'])
  },
  data(){
    return{
      activate_edit_modal: false,
      chosen_message: '',
      chosen_message_id: null,
      activate_delete_modal: false,
    }
  },
  methods:{
    change_messagebox(url){
      // uses next_url or previous_url  to fetch different messages
      if(url !== null){
        axios.get(url).then(response=>{
          this.$store.commit('fetch_message_box',{
            messages: response.data.results,
            next: response.data.next,
            previous: response.data.previous
          })
        })
      }
    },
    edit_message_activation(message_object){
      this.activate_edit_modal = !this.activate_edit_modal
      this.chosen_message_id = message_object.id
      this.chosen_message = message_object.msg
    },
    delete_message_activation(message_object){
      this.activate_delete_modal = !this.activate_delete_modal
      this.chosen_message_id = message_object.id
      this.chosen_message = message_object.msg
    },
    edit_message(){
       axios.put(`admin_panel/message_box/update/${this.chosen_message_id}/`,{
        msg: this.chosen_message // NOTE: this.chosen_message will be the most updated message from modal textarea
      }, {headers: {Authorization: `Bearer ${this.accessToken}`}}).then((response)=>{
        this.activate_edit_modal = false
        let msg_changed = this.messageboxes.filter(msg=> msg.id === this.chosen_message_id)
        msg_changed.msg = response.data.msg
        console.log(msg_changed)
      })
    },
    delete_message(){
      axios.delete(`admin_panel/message_box/update/${this.chosen_message_id}/`,
      {headers: {Authorization: `Bearer ${this.accessToken}`}}).then(response=>{
        toast({
          message: response.data.success,
          type: "is-success",
          dismissible: true,
          pauseOnHover: true,
          duration: 6000, // milliseconds
          position: "bottom-right",
        })
        this.activate_delete_modal = !this.activate_delete_modal
      })
    }
  }
}
</script>