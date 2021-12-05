<template>
  <section class="hero is-medium is-primary">
    <div class="hero-body">
      <div class="columns is-centered">
        <!-- Information Column -->
        <div class="column container is-10">
          <div class="box">
            <div class="title is-2 has-text-black">
                Shipping Details
            </div>
            <p class="help has-text-grey">
              * All fields are required
            </p>
            <div class="field">
              <div class="columns">
                <div class="column control">
                  <label>
                    First Name*
                  </label>
                  <input class="input" type="text" placeholder="First Name" v-model="first_name">
                </div>
                 <div class="column control">
                  <label>
                    Last Name*
                  </label>
                  <input class="input" type="text" placeholder="Last Name" v-model="last_name">
                </div>
              </div>
              <div class="columns">
                <div class="column control is-5">
                  <label>
                    Address*
                  </label>
                  <input class="input" type="text" placeholder="Address" v-model="address">
                </div>
                <div class="column control is-3">
                  <label>
                    City*
                  </label>
                  <input class="input" type="text" placeholder="City" v-model="city">
                </div>
                 <div class="column control">
                  <label>
                    Zip Code*
                  </label>
                  <input class="input" type="text" placeholder="Zip Code" v-model="zip_code">
                </div>
              </div>
              <div class="columns">
                <div class="column is-5 control">
                  Country*
                  <div class="select">
                    <select v-model="chosen_country">
                      <option
                        v-for="(country, index) in countries"
                        :key="index"
                      >
                        {{ country }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="column is-5 control">
                   State*
                  <div class="select">
                    <select v-model="chosen_state">
                       <option
                        v-for="(state, index) in country_states"
                        :key="index"
                      >
                        {{ state }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
              <p class="help is-danger" v-for="(error, index) in errors" :key="index">
                {{ error }}
              </p>
              <button class="button is-dark" @click="submit_shipping_details">
                Pay With Stripe
              </button>
            </div>
          </div>
        </div>
        <div class="is-divider-vertical"></div>
        <!-- Item Column -->
        <div class="column container is-3">
          <div class="box">
            <div class="title is-2 has-text-black">
                Your Items
            </div>
            <article class="media" v-for="(cart_item, index) in cart.items" :key="index">
              <figure class="media-left">
                <p class="image is-64x64">
                  <img :src="cart_item.photo" alt="Product-Image">
                </p>
              </figure>
              <div class="media-content ">
                <p class="title is-4 has-text-black">
                  {{ cart_item.name }}
                </p>
                <p class="subtitle is-6 has-text-black">
                  <strong class="has-text-black">Quantity: </strong>{{ cart_item.quantity }}
                  <br>
                  <strong class="has-text-black">Total Price: $</strong>{{ cart_item.price }}
                </p>
              </div>
            </article>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex';
import Cookies from 'cookies-js';
import countries_and_states from "../assets/Profile/countries_and_states";

export default{
  name: "Checkout",
  data(){
    return{
      states: [],
      countries: [],
      chosen_state: '',
      chosen_country:'',
      first_name: '',
      last_name: '',
      address: '',
      city: '',
      zip_code: '',
      errors: [],
    }
  },
  computed:{
    ...mapState(["cart"]),
    country_states() {
      let country_selected = {};
      if (this.chosen_country) {
        let state_obj = this.states.filter(
          (country) => country.country === this.chosen_country
        );
        if(state_obj[0]){
          country_selected = state_obj[0].states; // the thing is we are getting an array back so we need to grab the first result
        }
      } else {
        country_selected = { states: "Please choose a country first!!" }; // We need this to make sure that country_states return something not null
      }
      return country_selected;
    },
  },
  methods:{
    submit_shipping_details(){
      // Handle individual missing fields
      if(this.first_name === ''){
        this.errors.push('* The first name field is missing!')
      }
      if(this.last_name === ''){
        this.errors.push('* The last name field is missing!')
      }
      if(this.address === ''){
        this.errors.push('* The address field is missing!')
      }
      if(this.city === ''){
        this.errors.push('* The city field is missing!')
      }
      if(this.zip_code === ''){
        this.errors.push('* The zip code field is missing!')
      }
      if(this.chosen_country === ''){
        this.errors.push('* The country field is missing!')
      }
      if(this.chosen_state === ''){
        this.errors.push('* The state field is missing!')
      }

      if(this.first_name && this.last_name && this.address && this.city && this.zip_code &&
        this.chosen_country && this.chosen_state){
        this.errors = [] // We are going to reset errors
        console.log('proceed')
      }
    }
  },
  created(){
    // We are going to set our model countries to the our country objects
    this.states = countries_and_states.countries;
    this.states.forEach((country) => {
      this.countries.push(country.country);
    });
    // Now let's take care of our signed in users. Their information will now appear in shipping details
    if(Cookies('accessToken')){
      console.log('yeah')
    }
  }

}
</script>