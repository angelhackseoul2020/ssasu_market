<template>
  <div id="app">
    <router-view 
      :width='width'
      :height='height'
      ref='arrange'
    />
  </div>
</template>

<script>
export default {
  data:()=>({
    width:0,
    height:0,
  }),
  methods:{
    onresize(){
      this.width = window.innerWidth
      this.height = window.innerHeight
      console.log('resize', this.width, this.height);
    }
  },
  created(){
    window.addEventListener('resize', this.onresize)
    this.onresize()
  }
}
</script>


<style>
* {
  margin: 0;
}
</style>