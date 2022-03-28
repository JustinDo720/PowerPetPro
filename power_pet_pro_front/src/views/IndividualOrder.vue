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
          <div class="columns">
            <div class="column">
              <div class="box has-background-transparent">
                <h1 class="title is-3 has-text-centered has-text-white">Items</h1>
                <div class="box has-background-white" v-for="(item, index) in items" :key="index">
                  <div class="columns">
                      <div class="column">
                          <div class="card-content" v-if="item.photo">
                            <div class="columns">
                              <div class="column">
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
                                        {{ item.name }} <span class="tag is-small is-info is-light is-rounded">
                                        x{{ item.quantity }}
                                      </span>
                                      </p>
                                    </router-link>
                                    <p class="subtitle is-6">
                                      Price: <strong>${{ item.price }}</strong>
                                    </p>
                                  </div>
                                </div>
                              </div>
                              <div class="column">
                                <div class="content">
                                  {{ item.short_description }}
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="card-content" v-else>
                            <div class="columns">
                              <div class="column">
                                <div class="content">
                                  <router-link
                                    :to="`/product_list/product_detail${item.get_absolute_url}`"
                                  >
                                    <h5 class="has-text-link">
                                      {{ item.name }}<span class="tag is-small is-info is-light is-rounded">x{{ item.quantity }}</span>
                                    </h5>
                                  </router-link>
                                  <p>
                                    Price: <strong>${{ item.price }}</strong>
                                  </p>
                                </div>
                              </div>
                              <div class="column">
                                <div class="content">
                                  {{ item.short_description }}
                                </div>
                              </div>
                            </div>
                          </div>
                      </div>
                  </div>
                </div>
                <nav class="pagination" role="navigation" aria-label="pagination">
                  <button class="button" v-if="previous_page" @click="update_items(previous_page)">Previous</button>
                  <button class="button" v-if="next_page" @click="update_items(next_page)">Next page</button>
                </nav>
              </div>
            </div>
            <div class="column">
              <div class="box has-background-transparent">
                <h1 class="title is-3 has-text-centered has-text-white">
                  Purchase Summary
                </h1>
                <div class="box has has-background-white">
                  <table class="table is-fullwidth">
                    <thead>
                      <tr>
                        <th>Item</th>
                        <th>Price</th>
                        <th>Total Item Price</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in all_items" :key="index">
                        <td>
                            {{ item.name }}
                          <span class="tag is-small is-info is-light is-rounded">{{ item.quantity }}</span>
                        </td>
                        <td>{{ item.price }}</td>
                        <td>{{ item.price * item.quantity }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="box has has-background-white has-text-centered">
                  Total Cost: <strong>${{ paid_amount }}</strong>
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
      items: [],  // Paginated Items from IndividualOrderItems API
      all_items: [], // All of the Items from IndividualOrder API
      date_created: null,
      next_page: null,
      previous_page: null,
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
    update_items(api_call){
      let config = { headers: { Authorization: `Bearer ${this.accessToken}`} }
      axios.get(api_call, config).then((response)=>{
        this.items = response.data.results
        if(response.data.next){
          this.next_page = response.data.next
        }
        if(response.data.previous){
          this.previous_page = response.data.previous
        }
      })
    }
  },
  computed:{
    accessToken(){
      return Cookies("accessToken")
    }
  },
  created() {
    let user_id = this.$route.params.id
    let order_id = this.$route.params.order_number
    let config = { headers: { Authorization: `Bearer ${this.accessToken}`} }
    axios.get(`profile/${user_id}/order/${order_id}/`, config).then((response)=>{
      let order_details = response.data
      this.order_number = order_details.id
      this.paid_amount = order_details.paid_amount
      this.all_items = order_details.items
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

      // We need to retrieve the paginated items
      axios.get(`profile/${user_id}/order/${order_id}/items/`, config).then((response)=>{
        this.items = response.data.results
        if(response.data.next){
          this.next_page = response.data.next
        }

        if(response.data.previous){
          this.previous_page = response.data.previous
        }
      })
    })
  },
};
</script>

<style scoped>
.box{
  background-color: cornflowerblue;
}
</style>
