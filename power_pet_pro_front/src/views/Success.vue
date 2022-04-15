<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>
        <p>
          Your order will be processed by our agents within the next 2 days. {{ message }} <span class="is-link">{{ email }}</span>.
          Please check your inbox for further information about your order.
        </p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Cookies from 'cookies-js'
export default {
  name: "Success",
  data(){
    return{
      message: '',
      email: ''
    }
  },
  mounted() {
    // We are just setting the title of the documents
    // document.title = "Success | Pet Power Pro";
    let data = {}
    let order_id = this.$route.params.order_id
    if(Cookies('user_id')){
      // This means our user is authenticated therefore we send in our user_id and order_email
      data['user_id'] = Cookies('user_id')
      data['order_email'] = Cookies('order_email')
    } else if (Cookies('anonymous_user_email')){
      data['anonymous_user_email'] = Cookies('anonymous_user_email')
    }
    axios.post(`checkout/order/${order_id}/success/`, data).then((response)=>{
      console.log(response.data)
      this.message = response.data.message
      this.email = response.data.email
    })
  },
};
</script>
