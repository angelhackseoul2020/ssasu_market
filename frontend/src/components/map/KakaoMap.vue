<template>
  <div :id="elementId" :style="{ width, height }">
    <!-- daum kakao map -->
  </div>
</template>

<script>
import Map from '@/services/map/KakaoMap'

export default {
  created(){
    var keySet = this.markers.map(
      (marker) => {
        return marker.cluster_key
      }
    )
    keySet = keySet.filter((key,index) => keySet.indexOf(key) !== index)
    this.clustering = keySet.map(
      (key,index) =>{
        return{
          key:key,
          color:'#918749',
          zIndex:index
        }
      }
    )
  },
  props: {
    elementId: {
      type: String,
      required: true,
    },
    markers: {
      type: Array,
      default () {
        return []
      },
      required: true,
    },
    width: {
      type: String,
      required: false,
      default: '100%',
    },
    height: {
      type: String,
      required: false,
      default: '640px',
    },
  },
  data () {
    return {
      map: null,
      search: false,
      clustering:[]
    }
  },
  watch: {
    markers: {
      handler () {
        if (typeof window === 'undefined') return // SSR
        this.initMap(this.markers)
      },
      immediate: true,
    },
  },
  methods: {
    async initMap (markers) {
      if (!this.map) {
        const map = new Map()
        await map.mount(this.elementId)
        map.addMarkerClusters(this.clustering)
        this.map = map
        this.search = map.openSearch
      } else {
        this.map.clearMarkers()
      }
      var clusterClick=()=>{
        console.log('KakaoMap cluster click');
        this.$emit('click-cluster')
      }
      this.map.addMarkers(
        markers.map(
          (marker) => {
            const { name, cluster_key, latitude, longitude } = marker
            return {
              lat:latitude,
              lng:longitude,
              clusterKey: cluster_key,
              title: name,
              onClick: () => {
                this.$emit('click-marker', marker)
              },
              clusterClick:()=>{
                this.$emit('click-cluster', marker)
                console.log('cluster click');
              }
            }
          }
        ), clusterClick
      )
    },
    setCenter (lat, lng) {
      this.map && this.map.setCenter({ lat, lng, maxLevel: 10 })
    },
    
  },
}
</script>

<style>
</style>