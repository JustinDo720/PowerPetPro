<template>
  <section class="hero is-small is-info">
    <div class="hero-body has-text-centered">
      <p class="title">
        Your Order Number: #{{ order_number }}
      </p>
      <p class="subtitle">
        Order Placed on: {{ dateParse(date_created) }}
      </p>
    </div>
  </section>
  <section class="section is-medium">
    <!-- Nesting tiles -->
    <div class="tile is-ancestor">
      <div class="tile is-parent">
        <div class="tile is-child box">
          <p class="title has-text-centered has-text-white">Items</p>
          <div class="box has-background-white" v-for="(item, index) in items" :key="index">
              <div class="columns">
                <div class="column">
                    <div class="card-content" v-if="item.photo">
                      <div class="media">
                        <div class="media-left">
                          <figure class="image is-64x64">
                            <img :src="item.photo" alt="product-image" />
                          </figure>
                        </div>
                        <div class="media-content">
                          <router-link
                            :to="`/product_list/product_detail${item.get_absolute_url}`"
                          >
                            <p class="title is-5 has-text-link">
                              {{ item.name }}
                            </p>
                          </router-link>
                          <p class="subtitle is-6">
                            ${{ item.price }} x{{ item.quantity }}
                          </p>
                        </div>
                      </div>
                    </div>
                    <div class="card-content" v-else>
                      <div class="content">
                        <div class="content">
                          <router-link
                            :to="`/product_list/product_detail${item.get_absolute_url}`"
                          >
                            <h5 class="has-text-link">
                              {{ item.name }}
                            </h5>
                          </router-link>
                          <p>${{ item.price }} x{{ item.quantity }}</p>
                        </div>
                      </div>
                    </div>
                  </div>
              </div>
          </div>
        </div>
      </div>

      <div class="tile is-3 is-parent is-vertical">
        <div class="tile is-child box">
          <p class="title has-text-centered has-text-white">Shipping Address</p>
          <div class="box has-background-white">
            <div v-for="(shipping_info, key, index) in shipping_address" :key="index">
              <strong>{{ key }}: </strong> {{ shipping_info }}
            </div>
          </div>
        </div>
        <div class="tile is-child box">
          <p class="title has-text-centered has-text-white">Personal Information</p>
          <div class="box has-background-white">
            <div v-for="(info, key, index) in personal_info" :key="index">
              <strong>{{ key }}: </strong> {{ info }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js"

export default {
  name: "IndividualOrder",
  data(){
    return{
      order_number: null,
      paid_amount: null,
      shipping_address: {},
      personal_info: {},
      items: [],
      date_created: null,
    }
  },
  methods:{
    dateParse(date) {
      if(date != null){
        let new_date = new Date(
        date.slice(0, 4),
        date.slice(5, 7) - 1,
        date.slice(8, 10)
      );
      var options = { month: "long" };
      let month = new Intl.DateTimeFormat("en-US", options).format(new_date);
      return `${month} ${new_date.getDate()} ${new_date.getFullYear()}`;
      }
    },
  },
  computed:{
    accessToken(){
      return Cookies("accessToken")
    }
  },
  created() {
    let user_id = this.$route.params.id
    let order_id = this.$route.params.order_number
    axios.get(`profile/${user_id}/order/${order_id}/`, {
      headers: { Authorization: `Bearer ${this.accessToken}`}
    }).then((response)=>{
      let order_details = response.data
      this.order_number = order_details.id
      this.paid_amount = order_details.paid_amount
      this.items = order_details.items
      this.date_created = order_details.created_at
      this.shipping_address = {
        "Address": order_details.address,
        "City": order_details.address,
        "State": order_details.address,
        "Zip Code": order_details.zipcode,
        "Country": order_details.country
      }
      this.personal_info = {
        "First Name": order_details.first_name,
        "Last Name": order_details.last_name,
        "Phone Number": order_details.phone,
        "Email": order_details.email
      }
    })
  },
};
</script>

<style scoped>
.box{
  background-color: cornflowerblue;
}
</style>
