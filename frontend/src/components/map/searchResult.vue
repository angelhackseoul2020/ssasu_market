<template>
  <div id="search">
    <search-list :markers="markers" />
  </div>
</template>

<script>
import SearchList from "./SearchList.vue";
export default {
  components: {
    SearchList
  },
  props: {
    markers: {
      type: Array
    }
  },
  mounted() {
    var search = document.getElementById("search");
    search.style.width = "400px";
    search.style.height = window.innerHeight - 80 + "px";
    search.style.top = "40px";
    search.style.borderRadius = "40px";
  }
};
</script>

<style>
#search {
  overflow-y: auto;
  overflow-x: visible;
  z-index: 10;
}
#search::-webkit-scrollbar {
  width: 1px;
}
#search::-webkit-scrollbar-thumb {
  border-radius: 3px;
  background-color: gray;
}
#search::-webkit-scrollbar-button {
  width: 0;
  height: 0;
}
</style>