<template>
  <div id="category_product" class="columns is-multiline">
    <ProductBox v-for="(product,index) in categoryProducts"
                :key="index"
                :product="product">
    </ProductBox>
  </div>
</template>
<script>
import axios from "axios";
import ProductBox from "../components/ProductBox";
export default{
  name:'Category',
  components:{
    ProductBox
  },
  data(){
    return{
      categoryProducts:{}
    }
  },
  methods:{
    grabCategoryDetails(){
      // Make sure you are using $route not $router for params catching. .category_slug is the : in router
      let category_slug = this.$route.params.category_slug
      axios.get(`/category_detail${category_slug}`).then((response)=>{
        this.categoryProducts = response.data
        console.log(this.categoryProducts) // now this should have the response.data array
      })
    }
  }
  ,
  created(){
    this.grabCategoryDetails()
  }
}
</script>