<template>
  <section class="hero is-fullheight is-warning">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Reset Password</p>
        <hr />
        <p class="subtitle">
          Please enter your email below for us to send you the reset link!
        </p>

        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="reset_password">
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
              <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="email"
                    placeholder="Confirm Email"
                    v-model="user_reemail"
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
                Reset Password
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
  name: "ResetPassword",
  data() {
    return {
      user_email: "",
      user_reemail: "",
      error_message: "",
    };
  },
  methods: {
    reset_password() {
      if (
        this.user_email &&
        this.user_reemail &&
        this.user_reemail === this.user_email
      ) {
        axios
          .post("auth/users/reset_password/", { email: this.user_email })
          .then((response) => {
            console.log(response);
            toast({
              message: "Please check your email to reset your password !!!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 60000, // milliseconds
              position: "bottom-right",
            });
            this.$router.push({ name: "Home" });
          })
          .catch((err) => {
            this.error_message = err.response.data[0];
          });
      } else if (this.user_email === "" || this.user_reemail === "") {
        this.error_message = "Please enter in your email or confirmation email";
      } else {
        this.error_message = "Your email and confirmation email does not match";
      }
    },
  },
};
</script>
