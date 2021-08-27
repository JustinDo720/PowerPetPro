<template>
  <div>

  </div>
</template>
<script>
import axios from "axios";

export default{
  name:'Category',
  data(){
    return{
      categoryDetails:{}
    }
  },
  methods:{
    grabCategoryDetails(){
      // Make sure you are using $route not $router for params catching. .category_slug is the : in router
      let category_slug = this.$route.params.category_slug
      axios.get(`/category_detail${category_slug}`).then((response)=>{
        console.log(response.data)
      })
    }
  }
  ,
  created(){
    this.grabCategoryDetails()
  }
}
</script>