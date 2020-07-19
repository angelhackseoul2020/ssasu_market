<template>
  <div id="search-list">
    <search-item v-for="marker in markers" :marker="marker" :key="marker" style="margin-top:10px" />
  </div>
</template>

<script>
import SearchItem from "./SearchItem.vue";
export default {
  props: {
    markers: {
      type: Array
    }
  },
  components: {
    SearchItem
  },
  mounted() {
    console.log(this.markers);
  }
};
</script>

<style>
#search-list {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>