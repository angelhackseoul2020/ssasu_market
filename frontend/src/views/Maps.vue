<template>
  <kakao-map
    elementId="map"
    :markers="markers"
    :width="mapwidth"
    :height="mapheight"
  />
</template>
<script>
import KakaoMap from '../components/map/KakaoMap.vue'
export default {
  data:()=>({
    beforeLogin:1,
    width:0,
    height:0,
    mapwidth:0,
    mapheight:0,
    markers:[
      { "name":"광장시장",
        "score":4,
        "type":"신림",
        "location":{
          "lat": 37.27943075229118,
          "lng": 127.01763998406159
        }
      },
      { "name":"옥련시장",
        "score":3,
        "type":"서울대입구",
        "location":{
          "lat": 37.27943075229118,
          "lng": 127.01763998406159
        }
      },
      { "name":"깡통시장",
        "type":"봉천",
        "score":5,
        "location":{
          "lat": 37.24943075229118,
          "lng": 127.01163998406159
        }
      },
      { "name":"남부시장",
        "type":"신림",
        "score":4.5,
        "location":{
          "lat": 37.21943375229118,
          "lng": 127.02764998406159
        }
      },
      { "name":"자갈치시장",
        "score":2.5,
        "location":{
          "lat": 37.27443075229118,
          "lng": 127.03763998406159
        }
      },
      { "name":"광명시장",
        "score":4,
        "location":{
          "lat": 37.25941075229118,
          "lng": 127.04762998406159
        }
      }
      ],
  })
  ,
  components: {
    KakaoMap, 
  },
  created(){
    this.width = window.innerWidth
    this.height = window.innerHeight
    this.mapwidth = this.width + 'px'
    this.mapheight = this.height + 'px'
  },
  methods:{
  },
}
</script>

<style>
#intro{
  position: absolute;
  top:0;
  left:0;
}
#map{
  position: absolute;
  top: 0;
  left:0;
}
#search{
    background-color: #ffffff;
    position: absolute;
    display: none;
    top:0;
    left: 10px;
}
input:focus{
    outline: none;
}
</style>