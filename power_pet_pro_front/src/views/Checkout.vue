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
                <div class="column control">
                  <label>
                    Email*
                  </label>
                  <input class="input" type="email" placeholder="Email" v-model="email">
                </div>
                 <div class="column control">
                  <label>
                    Phone Number*
                  </label>
                  <input class="input" type="text" placeholder="Phone Number" v-model="phone_number">
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
              <div class="columns">
                <div class="column control">
                   <div ref="card" class="mb-5 form-control"></div>
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
                  <strong class="has-text-black">Total Price: $</strong>{{ cart_item.price * cart_item.quantity }}
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
import axios from 'axios';

export default{
  name: "Checkout",
  data(){
    return{
      stripe: {},
      card: {},
      states: [],
      countries: [],
      chosen_state: 'New York',
      chosen_country:'United States',
      first_name: 'Justin',
      last_name: 'Do',
      email: 'justindo720@gmail.com',
      phone_number: '929282158575',
      address: '1175 Arnow Ave',
      city: 'Bronx',
      zip_code: '10469',
      errors: [],
    }
  },
  computed:{
    ...mapState(["cart", "accessToken"]),
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
      if(this.email === ''){
        this.errors.push('* The email field is missing!')
      }
      if(this.phone_number === ''){
        this.errors.push('* The phone number field is missing!')
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

      if(!this.errors.length){
        this.$store.commit('setIsLoading', true)
        this.stripe.createToken(this.card).then(result=>{
          if(result.error){
            this.$store.commit('setIsLoading', false)
            this.errors.push('Something went wrong with Stripe. Please try again')
            console.log(result.error.message)
          } else {
            console.log(result.token.id)
            this.stripeTokenHandler(result.token)
          }
        })
      }else{
        console.log(this.errors)
      }
    },
    async stripeTokenHandler(token){
      const items = []
      // We just need to loop over the item in our cart and push it in our const items variable
      for(let i=0; i < this.cart.items.length; i++){
        const curr_item = this.cart.items[i]
        const obj = {
          product: curr_item.product, // we are getting the id of the product for our db to read it
          quantity: curr_item.quantity,
          price: curr_item.price * curr_item.quantity // total price
        }
        items.push(obj)
      }
      const data = {
        'first_name': this.first_name,
        'last_name': this.last_name,
        'email': this.email,
        'address': this.address,
        'zipcode': this.zip_code,
        'phone': this.phone_number,
        'city': this.city,
        'country': this.chosen_country,
        'state': this.chosen_state,
        'items': items,
        'stripe_token': token.id
      }

      await axios.post('checkout/', data, {headers: {
        Authorization: `Bearer ${this.accessToken}`
        }}).then(response=>{
          this.$store.commit('clearCart')
          this.$router.push({name:'Success'})
      }).catch(err=>{
        this.errors.push('Something went wrong. Please try again.')
      })

      // We need to set loading off because we initially set it true in submit_shipping_details
      this.$store.commit('setIsLoading', false)
    }
  },
  created(){
    // We are going to set our model countries to the our country objects
    this.states = countries_and_states.countries;
    this.states.forEach((country) => {
      this.countries.push(country.country);
    });
    // Now let's take care of our signed in users. Their information will now appear in shipping details
    if(Cookies('accessToken') && Cookies('user_id')){
      axios.get(`profile_list/user_profile/${Cookies('user_id')}/`, {
        headers: {Authorization: `Bearer ${Cookies('accessToken')}`}
      }).then(response=>{
        this.first_name = response.data.first_name
        this.last_name = response.data.last_name
        this.address = response.data.address
        this.zip_code = response.data.zip_code
        this.city = response.data.city
        this.chosen_country = response.data.country
        this.chosen_state = response.data.state
        this.email = response.data.email
        this.phone_number = response.data.phone_number
      })
    }
  },
  mounted(){
    document.title = 'Checkout | Power Pet Pro'
    // we create an instance of stripe and we use window because of index.html with our stripe cdn
    this.stripe =  window.Stripe(process.env.VUE_APP_STRIPE_TOKEN)
    // We need to create an instance of elements
    const elements = this.stripe.elements();
    // Just styling for stripe which we will add when we create an element of card
    const style = {
      base: {
        color: '#32325d',
        lineHeight: '24px',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
          color: '#aab7c4'
        }
      },
      invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
      }
    }
    // Creating an element of card with some options like style and hidePostalCode
    this.card = elements.create('card', { hidePostalCode: true, style: style})
    // Once we finish creating an instance of stripe of elements and binding them to this.card we mount it
    this.card.mount(this.$refs.card) // this.$refs.card just mounts it to the div that has ref='card'
  },

}
</script>

<style scoped>
/* Although we dont use the class StripeElement stripe actually puts class='StripeElement' wherever card is mounted */
.StripeElement {
  background-color: white;
  padding: 8px 12px;
  border-radius: 4px;
  border: 1px solid transparent;
  box-shadow: 0 1px 3px 0 #e6ebf1;
  -webkit-transition: box-shadow 150ms ease;
  transition: box-shadow 150ms ease;
}

.StripeElement--focus {
  box-shadow: 0 1px 3px 0 #cfd7df;
}

.StripeElement--invalid {
  border-color: #fa755a;
}

.StripeElement--webkit-autofill {
  background-color: #fefde5 !important;
}
</style>