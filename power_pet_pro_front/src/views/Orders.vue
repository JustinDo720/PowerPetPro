<template>
  <section class="section is-small">
     <h1 class="title is-1 has-text-centered">
          Your orders
      </h1>
    <div class="columns is-centered">
      <div class="column is-5">
        <div class="box">
          <div v-for="(order, key) in orders" :key="key">
            <div class="card">
              <header class="card-header">
                <p class="card-header-title">
                  Order #{{ order.id }}
                </p>
                 <p class="card-header-title">
                  Total ${{ order.paid_amount }}
                </p>
              </header>
              <div v-for="(order_item, key) in order.items.slice(0,2)" :key="key" class="columns">
                <div class="card-content column" v-if="order_item.photo">
                    <div class="media">
                      <div class="media-left">
                        <figure class="image is-64x64">
                          <img :src="order_item.photo" alt="product-image">
                        </figure>
                      </div>
                      <div class="media-content">
                        <router-link :to="`/product_list/product_detail${order_item.get_absolute_url}`">
                          <p class="title is-5 has-text-link">
                            {{ order_item.name }}
                          </p>
                        </router-link>
                        <p class="subtitle is-6"> ${{ order_item.price }} x{{ order_item.quantity }}</p>
                      </div>
                    </div>
                </div>
                <div class="card-content column" v-else>
                  <div class="content">
                    <div class="content">
                      <router-link :to="`/product_list/product_detail${order_item.get_absolute_url}`">
                        <h5 class="has-text-link">
                          {{ order_item.name }}
                        </h5>
                      </router-link>
                      <p>
                        ${{ order_item.price }}
                        x{{ order_item.quantity }}
                      </p>
                    </div>
                  </div>
                </div>
                <div class="card-content column">

                </div>
              </div>
            </div>
            <br>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js";

export default{
  name: 'Orders',
  data(){
    return{
      orders: [],
    }
  },
  computed:{
     accessToken() {
      return Cookies("accessToken");
    },
  },
  created(){
    let user_id = this.$route.params.id
    axios.get(`orders/${user_id}/`,{
      headers: { Authorization: `Bearer ${this.accessToken}`}
    }).then((response)=>{
      this.orders = response.data.results
    })
  }
}
</script>