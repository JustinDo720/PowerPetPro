<template>
  <section class="hero is-halfheight heroImage">
    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="card card-shadow">
          <div class="card-content">
              <h2 class="title is-2 has-text-centered">
                Our Mission
              </h2>
              <hr>
            <div class="content">
              Lorem ipsum leo risus, porta ac consectetur ac, vestibulum at eros. Donec id elit non mi porta gravida at eget metus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras mattis consectetur purus sit amet fermentum.
            </div>
          </div>
          <footer class="card-footer">
            <a href="#" class="card-footer-item">Save</a>
            <a href="#" class="card-footer-item">Edit</a>
            <a href="#" class="card-footer-item">Delete</a>
          </footer>
        </div>
    </div>
  </div>

  </section>
</template>

<script>

export default{
  name: 'HomeMission',
  data(){
    return{

    }
  },

}
</script>

<style scoped>
.heroImage{
  background-image: url('../../assets/dog_friend.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;

}
</style>
