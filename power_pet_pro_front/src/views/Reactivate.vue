<template>
  <section class="hero is-fullheight is-warning">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Resend Activation Link</p>
        <hr />
        <p class="subtitle">
          Please enter your email below for us to send you the reactivation
          link!
        </p>

        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="resend_activation_email">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="email"
                    placeholder="Email"
                    v-model="user_email"
                  />
                </div>
              </div>

              <div v-if="error_message">
                <p class="help is-danger">
                  {{ error_message }}
                </p>
              </div>
              <br />

              <button class="button is-warning" type="submit">
                Resend Activation Email
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Reactivate",
  data() {
    return {
      user_email: "",
      error_message: "",
    };
  },
  methods: {
    resend_activation_email() {
      axios
        .post("auth/users/resend_activation/", {
          email: this.user_email,
        })
        .then(() => {
          toast({
            message: "Please check your email for the activation link!!!",
            type: "is-success",
            dismissible: true,
            pauseOnHover: true,
            duration: 60000, // milliseconds
            position: "bottom-right",
          });
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err.response);
          this.error_message = err.response.data[0];
        });
    },
  },
};
</script>
