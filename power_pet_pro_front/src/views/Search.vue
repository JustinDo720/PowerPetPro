<template>
  <div class="columns">
    <div class="column is-12 has-text-centered">
      <h1 class="title is-2">
        Search Term: "{{ searchTerm }}"
      </h1>
    </div>
    <div class="column" v-for="(product, index) in products" :key="index">
      {{ product }}
    </div>
  </div>
</template>

<script>
// import ProductBox from "../components/ProductBox";
import axios from "axios";
import { mapState } from 'vuex';

export default{
  name: 'Search',
  components:{
    // ProductBox
  },
  computed:{
    ...mapState(['searchTerm'])
  },
  data(){
    return{
      products: [],
    }
  },
  mounted(){
    axios.post('/product_list/search/', {'query':this.searchTerm}).then((response)=>{
      this.products = response.data
      console.log(this.products)
    })
  },
  methods:{

  }

}
</script>