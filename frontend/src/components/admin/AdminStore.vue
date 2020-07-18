<template>
  <div class="adminStoreWrap">
    <store-add-modal v-if="storeAddModal"
      :data=stores[selAddModal]
      @closeModal="closeModal"
    />
    <div id="storeFilter">
      <input type="text" id="storeLocation" autocomplete="off" placeholder="지역" v-model="locFilter">
      <input type="text" id="storeMarket" autocomplete="off" placeholder="시장" v-model="marketFilter">
      <input type="text" id="storeSort" autocomplete="off" placeholder="종류" v-model="sortFilter">
      <button id="addStoreBtn">상점추가</button>
    </div>
    <div id="storeList">
      <row
        :id="header.id"
        :name="header.name"
        :sort="header.sort"
        :address="header.address"
        :market="header.market"
      />
      <row v-for="(store,index) in filtered" :key="index" @openModalStore="openModalStore"
        :id="store.id"
        :index="index"
        :name="store.name"
        :sort="store.sort"
        :address="store.address"
        :market="store.market"
      />
    </div>
  </div>
</template>

<script>
import row from './storeRow'
import storeAddModal from './AdminStoreAdd'

export default {
  name: "AdminStore",
  components: {row, storeAddModal},
  methods:{
    openModalStore(index){
      console.log(index);
      this.selAddModal = index
      this.storeAddModal = 1
    },
    closeModal(){
      this.selAddModal = -1
      this.storeAddModal = 0
    }
  },
  data(){
    return{
      storeAddModal:0,
      selAddModal:-1,
      locFilter:'',
      marketFilter:'',
      sortFilter:'',
      filtered:[],
      header:{
        id:'ID',
        name:'상점이름',
        sort:'종류',
        address:'주소',
        market:'시장'
      },
      stores:[
        {
          id:'1',
          name:'신원 청과',
          sort:'청과',
          address:'서울시 관악구 신림동',
          market:'신원시장',
        },
        {
          id:'2',
          name:'영일 축산',
          sort:'축산',
          address:'서울시 관악구 신림동',
          market:'신원시장',
        },
        {
          id:'3',
          name:'대명 마트',
          sort:'마트',
          address:'서울시 금천구 대명동',
          market:'대명시장',
        },
      ],
    }
  },
  mounted(){
    this.filtered = this.stores
  },
  watch:{
    locFilter:{
      handler(e){
        this.filtered = this.stores.filter((store)=>{
          var loc = store.address.split(' ')
          var result = false
          for (var l of loc){
            if (e === l.slice(0,e.length)){
              result = true
              break
            }
          }
          return result
        })
      }
    },
    marketFilter:{
      handler(e){
        this.filtered = this.stores.filter((store)=>
          e === store.market.slice(0,e.length)
        )
      }
    },
    sortFilter:{
      handler(e){
        this.filtered = this.stores.filter((store)=>
          e === store.sort.slice(0,e.length)
        )
      }
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.adminStoreWrap {
  position: relative;
  margin: 3rem 3rem;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
}
.addStore {
  background-color: #fdafd063;
  outline: 0;
  width: 130px;
  font-size: 1.6rem;
  color: #2e0202;
  border-style: none;
  border-radius: 40px;
}
.addStore:hover {
  cursor: pointer;
}
#storeFilter{
  position: absolute;
  width: 100%;
  top:50px;
}
#storeLocation{
  width: 180px;
  height: 50px;
  font-size: 2rem;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
  margin-left: 30px;
}
#storeMarket{
  width: 250px;
  height: 50px;
  font-size: 2rem;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  margin-left: 30px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#storeSort{
  width: 180px;
  height: 50px;
  font-size: 2rem;
  margin-left: 30px;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
Input{
  outline: 0;
}
#addStoreBtn{
  position: absolute;
  width: 180px;
  right:30px;
  height: 50px;
  font-size: 2rem;
  margin-left: 30px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
  outline: 0;
  cursor: pointer;
}
#storeList{
  position: absolute;
  width: 100%;
  top: 20%
}

</style>