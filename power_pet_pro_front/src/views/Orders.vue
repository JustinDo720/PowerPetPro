<template>
  <section class="section is-small">
     <h1 class="title is-1 has-text-centered">
          Your Orders
      </h1>
    <div class="columns is-centered">
      <div class="column is-7">
        <div class="box">
          <OrderBox
              v-for="(order, index) in orders"
              :key="index"
              :order="order"
          ></OrderBox>
          <br>
          <OrderPagination
              :previous_page="previous_page"
              :next_page="next_page"
              @change_orders="change_order($event)"
          ></OrderPagination>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
import Cookies from "cookies-js";
import OrderBox from "../components/OrderBox";
import OrderPagination from "../components/OrderPagination";

export default{
  name: 'Orders',
  components:{
    OrderBox,
    OrderPagination,
  },
  data(){
    return{
      orders: [],
      previous_page: null,
      next_page: null,
    }
  },
  methods:{
    grab_data(api_url){
      axios.get(api_url,{
        headers: { Authorization: `Bearer ${this.accessToken}`}
      }).then((response)=>{
        this.orders = response.data.results
        this.previous_page = response.data.previous
        this.next_page = response.data.next
      })
    },
    change_order(new_orders_obj){
      this.orders = new_orders_obj.results
      this.previous_page = new_orders_obj.previous
      this.next_page = new_orders_obj.next
    }
  },
  computed:{
     accessToken() {
      return Cookies("accessToken");
    },
  },
  created(){
    this.user_id = this.$route.params.id
    let api_url = `profile/${this.user_id}/orders/`
    this.grab_data(api_url)
  }
}
</script>