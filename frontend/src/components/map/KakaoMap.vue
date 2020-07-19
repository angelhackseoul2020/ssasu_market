<template>
  <div :id="elementId" :style="{ width, height }">
    <!-- daum kakao map -->
  </div>
</template>

<script>
import Map from "@/services/map/KakaoMap";

export default {
  mounted() {},
  props: {
    elementId: {
      type: String,
      required: true
    },
    markers: {
      type: Array,
      default() {
        return [];
      },
      required: true
    },
    width: {
      type: String,
      required: false,
      default: "100%"
    },
    height: {
      type: String,
      required: false,
      default: "640px"
    }
  },
  data() {
    return {
      map: null,
      search: false,
      clustering: []
    };
  },
  watch: {
    markers: {
      handler() {
        if (typeof window === "undefined") return; // SSR
        var keySet = this.markers.map(marker => {
          return marker.cluster_key;
        });
        keySet = keySet.filter((key, index) => keySet.indexOf(key) !== index);
        this.clustering = keySet.map((key, index) => {
          return {
            key: key,
            color: "#345671",
            zIndex: index
          };
        });
        this.initMap(this.markers);
      },
      immediate: true
    }
  },
  methods: {
    async initMap(markers) {
      if (!this.map) {
        const map = new Map();
        await map.mount(this.elementId);
        map.addMarkerClusters(this.clustering);
        this.map = map;
        this.search = map.openSearch;
      } else {
        this.map.clearMarkers();
      }
      var clusterClick = () => {
        console.log("KakaoMap luster clik");
        this.$emit("click-cluster");
      };
      this.map.addMarkers(
        markers.map(marker => {
          const {
            address,
            avg_score,
            image,
            id,
            name,
            cluster_key,
            latitude,
            longitude,
            parking,
            phone,
            road_address,
            store_num,
            toilet,
            url
          } = marker;
          return {
            address,
            avg_score,
            image,
            id,
            parking,
            phone,
            road_address,
            store_num,
            toilet,
            url,
            lat: latitude,
            lng: longitude,
            clusterKey: cluster_key,
            title: name,
            onClick: () => {
              this.$emit("click-marker", marker);
            },
            clusterClick: () => {
              this.$emit("click-cluster", marker.cluster_key);
            }
          };
        }),
        clusterClick
      );
    },
    setCenter(lat, lng) {
      this.map && this.map.setCenter({ lat, lng, maxLevel: 10 });
    }
  }
};
</script>

<style>
</style>