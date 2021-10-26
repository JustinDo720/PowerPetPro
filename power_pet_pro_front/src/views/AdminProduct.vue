<template>
  <section class="hero is-fullheight ">
    <div class="hero-body">
      <div class="container has-text-centered">
        <p class="title is-1">Adding A Product</p>
        <hr />
        <p class="subtitle">Please Enter the follow information below to add a product</p>

        <div class="columns is-centered">
          <div class="column is-5">
            <form class="box" @submit.prevent="submit_product()">
              <figure class="image is-128x128 is-inline-block">
                <img
                  class="is-square"
                  alt="ppp-logo"
                  src="../assets/ppp_logo.jpg"
                />
              </figure>
              <div class="field">
                  <h1 class="title is-4">Category: </h1>
                  <div class="select is-medium is-rounded">
                    <select v-model="chosen_category">
                      <option v-for="(category, index) in store_categories" :key="index" >
                        {{ category.name }}
                      </option>
                    </select>
                  </div>
              </div>
              <div class="field">
                  <input
                    class="input is-medium"
                    type="text"
                    placeholder="Product Name"
                    v-model="product_name"
                  />
              </div>

               <div class="field">
                <div class="control has-icons-left">
                  <span class="icon is-medium is-left">
                    <i class="fas fa-tags"></i>
                  </span>
                  <input
                    class="input is-medium"
                    type="number"
                    placeholder="Product Price"
                    v-model="product_price"
                  />
                </div>
              </div>

              <button class="button is-success">Submit Product</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default{
  name: "AdminProduct",
  data(){
    return{
      chosen_category : '',
      product_name : '',
      product_price: 0,
    }
  },
  methods:{
    submit_product(){
      if(this.chosen_category && this.product_name && this.product_price){
        // if these exists then we are going to submit the product
      }
    }
  },
  computed:{
    ...mapState(['store_categories'])
  },
  created(){
    console.log(this.store_categories)
  }
}
</script>
