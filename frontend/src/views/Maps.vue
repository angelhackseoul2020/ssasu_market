<template>
  <div>
    <kakao-map
      elementId="map"
      :markers="markers"
      :width="mapwidth"
      :height="mapheight"
      @click-cluster="openCluster"
    />
    <search-result :markers="clusterMarkers" />
  </div>
</template>
<script>
import KakaoMap from "../components/map/KakaoMap.vue";
import SearchResult from "../components/map/searchResult.vue";
import axios from "axios";
export default {
  data: () => ({
    beforeLogin: 1,
    width: 0,
    height: 0,
    mapwidth: 0,
    mapheight: 0,
    markers: [],
    clusterMarkers: []
  }),
  components: {
    KakaoMap,
    SearchResult
  },
  created() {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.mapwidth = this.width + "px";
    this.mapheight = this.height + "px";
    axios.get("http://127.0.0.1:8000/market/info/").then(response => {
      console.log("maps", response);
      this.markers = response.data;
    });
  },
  mounted() {},
  methods: {
    openMarker() {},
    openCluster(event) {
      console.log("maps", event);
      var search = document.getElementById("search");
      this.clusterMarkers = this.markers.filter(
        val => val.cluster_key === event
      );
      console.log(this.clusterMarkers);
      setTimeout(() => {
        search.style.display = "block";
      }, 10);
    }
  }
};
</script>

<style>
#intro {
  position: absolute;
  top: 0;
  left: 0;
}
#map {
  position: absolute;
  top: 0;
  left: 0;
}
#search {
  background-color: #ffffff;
  position: absolute;
  display: none;
  top: 0;
  left: 10px;
}
input:focus {
  outline: none;
}
</style>