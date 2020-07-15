<template>
  <div :id="elementId" :style="{ width, height }">
    <!-- daum kakao map -->
  </div>
</template>

<script>
import Map from '@/services/map/KakaoMap'

export default {
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
      search: false
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
        map.addMarkerClusters([
          {
            key: '신림',
            color: '#222529',
            zIndex: 0,
            singleIconURL: '../assets/logo.png',
          },
          {
            key: '봉천',
            color: '#209cee',
            zIndex: 1,
            singleIconURL: '../assets/logo.png',
          },
          {
            key: '서울대입구',
            color: '#209fef',
            zIndex: 2,
            singleIconURL: '../assets/logo.png',
          },
        ])
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
            const { name, type, location: { lat, lng } } = marker
            return {
              lat,
              lng,
              clusterKey: type,
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