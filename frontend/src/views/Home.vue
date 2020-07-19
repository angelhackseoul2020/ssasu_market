<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/imgs/logo1.png">
    <HelloWorld msg="인트로 페이지"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
