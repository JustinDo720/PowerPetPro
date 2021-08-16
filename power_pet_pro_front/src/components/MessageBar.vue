<template>
    <div class="container is-fluid messageBackground">
        <div>
          <p class="whiteText">
            This container is <strong>centered</strong> on desktop and larger viewports.
          </p>

        </div>
    </div>
</template>

<script>

export default{
  name: 'MessageBar'
}

</script>

<style scoped>
.messageBackground{
  background-color: black;
  justify-content: center;
  display:flex;
}
.whiteText{
  color:white;
}
</style>