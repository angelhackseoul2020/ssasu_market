<template>
  <div id="adminStoreAddWrap">
    <div id="adminStoreAddLabel">
      <p id="storeNameText">상점이름</p>
      <p id="storeDetailSetText">지역 / 시장 / 종류</p>
      <p id="storeAddressText">주소</p>
      <p id="storeTellText">연락처</p>
      <p id="storeOpenCloseText">영업시간<br>(open / close)</p>
      <p id="storeMemoText">메모</p>
    </div>
    <div id="adminStoreAdd">
      <form action method="GET">
        <input type="text" id="storeName" placeholder="상점 이름" required/>
        <input type="text" id="storeLocation" placeholder="지역" v-model="selLoc" autocomplete="off">
        <div id="storeLocSelect" v-if="location">
          <div id="LocSelectBox" v-for="(loc, index) in sumLoc" :key="index" @mouseover="selectLoc(loc)">{{loc}}</div>
        </div>
        <input type="text" id="storeMarket" placeholder="시장" v-model="selMarket" autocomplete="off">
        <div id="storeMarketSelect" v-if="market">
          <div id="MarketSelectBox" v-for="(mk, index) in sumMarket" :key="index" @mouseover="selectMarket(mk)">{{mk}}</div>
        </div>
        <input type="text" id="storeAddress" placeholder="주소" />
        <input type="text" id="storeTell" placeholder="연락처" />
        <div id="storeOpen" v-if="!open">
          <div id="storeOpenBtn"></div>
          {{selOpen}}
        </div>
        <div id="storeOpenSel" v-else>
          <div id="storeOpenSelItem" v-for="time in opentime" :key="time" @click="openTimeSelect(time)">
            {{time}}
          </div>
        </div>
        <div id="storeClose" v-if="!close">
          <div id="storeOpenBtn"></div>
          {{selClose}}
        </div>
        <div id="storeCloseSel" v-else>
          <div id="storeCloseSelItem" v-for="time in closetime" :key="time" @click="closeTimeSelect(time)">
            {{time}}
          </div>
        </div>

        <input type="text" id="storeMemo" placeholder="메모" />
        <div class="deleteSave">
          <button type="button" id="delete" @click="$emit('closeModal')">delete</button>
          <button type="button" id="save">save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminStore",
  props:{
    data:{type:Object, default:{}}
  },
  components: {},
  mounted(){
    this.sumLoc = this.locations
    this.sumMarket = this.markets
    var storeName = document.getElementById('storeName')
    storeName.value = this.data.name
    var selectLocBox = document.getElementById('storeLocation')
    selectLocBox.addEventListener('focusin',()=>{
      this.selLoc = ''
      this.pickLoc = ''
      this.location = true
    })
    selectLocBox.addEventListener('focusout',()=>{
      if (this.pickLoc){
        this.selLoc = this.pickLoc
      }
      this.location = false
    })
    selectLocBox.addEventListener('keydown',(e)=>{
      if(e.key === 'Enter'){
        selectLocBox.blur()
        this.selLoc = this.sumLoc[0]
      }
    })
    var selectMarketBox = document.getElementById('storeMarket')
    selectMarketBox.addEventListener('focusin',()=>{
      this.selMarket = ''
      this.pickMarket = ''
      this.market = true
    })
    selectMarketBox.addEventListener('focusout',()=>{
      if (this.pickMarket){
        this.selMarket = this.pickMarket
      }
      this.market = false
    })
    selectMarketBox.addEventListener('keydown',(e)=>{
      if(e.key === 'Enter'){
        selectMarketBox.blur()
        this.selMarket = this.sumMarket[0]
      }
    })
    var OpenTimeSelect = document.getElementById('storeOpen')
    OpenTimeSelect.addEventListener('click',()=>{
      this.open = true
    })
    var CloesTimeSelect = document.getElementById('storeClose')
    CloesTimeSelect.addEventListener('click',()=>{
      this.close = true
    })
  },
  methods:{
    selectLoc(i){
      this.pickLoc = i 
    },
    selectMarket(i){
      this.pickMarket = i
    },
    openTimeSelect(i){
      this.selOpen = i
      setTimeout(() => {
        this.open = false
      }, 100);
    },
    closeTimeSelect(i){
      this.selClose = i
      setTimeout(() => {
        this.close = false
      }, 100);
    }
  },
  data:()=>({
    locations:['강남구', '강서구', '관악구', '영등포구', '구로구', '금천구'],
    sumLoc:[],
    location:0,
    selLoc:'',
    pickLoc:'',
    markets:['광장시장광장시장광장시장', '어떤시장', '이런시장', '저런시장', '광명시장'],
    sumMarket:[],
    market:0,
    selMarket:'',
    pickMarket:'',
    allClose:0,
    sort:0,
    selSort:0,
    opentime:['05시', '06시', '07시', '08시', '09시', '10시', '11시', '12시'],
    open:0,
    selOpen:'00시',
    closetime:['16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시', '24시'],
    close:0,
    selClose:'24시',
  }),
  watch:{
    allClose:{
      handler(value){
        if (value === 0){
          this.location = 0,
          this.market = 0,
          this.sort = 0,
          this.open = 0,
          this.close = 0
        }
      }
    },
    selLoc:{
      handler(value){
        console.log(value);
        this.sumLoc = this.locations.filter((loc) => value === loc.slice(0,value.length))
      }
    },
    selMarket:{
      handler(value){
        this.sumMarket = this.markets.filter((mk) => value === mk.slice(0,value.length))
      }
    },
    immediate:true
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
#adminStoreAddWrap {
  width: 90%;
  height: 90%;
  position:relative;
  margin: 3rem 3rem;
  background-color: rgb(252, 252, 252);
  border-radius: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 20;
}
#adminStoreAddLabel{
  position: absolute;
  width:30%;
  height:100%;
  left: 0;
}
#storeNameText{
  position:absolute;
  font-size: 40px;
  right: 0;
  top:50px;
}
#storeDetailSetText{
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 150px;
}
#storeAddressText{
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 250px;
}
#storeTellText{
  position: absolute;
  font-size: 40px;
  right:0;
  top:350px;
}
#storeOpenCloseText{
  position: absolute;
  font-size: 30px;
  right: 0;
  top:450px;
  text-align: end;
}
#storeMemoText{
  position: absolute;
  font-size: 40px;
  right: 0;
  top:570px
}
#adminStoreAdd {
  position:absolute;
  width: 70%;
  height: 100%;
  left:30%
}
#storeName{
  position: absolute;
  top:50px;
  left: 30px;
}
#storeLocation{
  position:absolute;
  top:152.4px;
  left: 30px;
  width: 150px;
  padding: 2px 0 2px 20px;
  height: 50px;
  font-size: 2rem;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#storeMarket{
  position: absolute;
  top: 152.4px;
  left: 200px;
  width: 360px;
  padding: 2px 0 2px 20px;
}
#storeMarketSelect{
  position:absolute;
  top:202.4px;
  left: 200px;
}

#downBtnLoc{
  position: absolute;
  width:15px;
  height: 15px;
  right: 15px;
  top: 15px;
  background-color: red;
}
#storeLocSelect{
  position:absolute;
  top:202.4px;
  left: 30px;
}
#LocSelectBox{
  position: relative;
  background-color: rosybrown;
  width: 150px;
  padding: 2px 0 2px 20px;
  height: 50px;
  font-size: 2rem;
  border-radius: 20px;
  z-index: 10;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#MarketSelectBox{
  position: relative;
  background-color: rosybrown;
  width: 360px;
  padding: 2px 0 2px 20px;
  height: 50px;
  font-size: 2rem;
  border-radius: 20px;
  z-index: 10;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#storeAddress{
  position: absolute;
  top:250px;
  left: 30px;
}

#storeTell{
  position:absolute;
  top:350px;
  left:30px;
}
#storeOpen{
  position: absolute;
  top: 465px;
  left: 30px;
  width: 130px;
  height: 50px;
  font-size: 2rem;
  padding: 4px 0 4px 20px;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#storeOpenBtn{
  position: absolute;
  top: 16px;
  width: 15px;
  height: 15px;
  background-color: red;
  right: 15px;
}
#storeClose{
  position: absolute;
  top: 465px;
  left: 180px;
  width: 130px;
  height: 50px;
  font-size: 2rem;
  padding: 4px 0 4px 20px;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
#storeOpenSel{
  position: absolute;
  top: 465px;
  left: 30px;
  }
#storeOpenSelItem{
  position: relative;
  width: 130px;
  height: 50px;
  font-size: 2rem;
  padding: 4px 0 4px 20px;
  padding-left: 20px;
  background-color: #fdafd0;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
  z-index: 10;
}
#storeCloseSel{
  position: absolute;
  top: 465px;
  left: 180px;
  }
#storeCloseSelItem{
  position: relative;
  width: 130px;
  height: 50px;
  font-size: 2rem;
  padding: 4px 0 4px 20px;
  padding-left: 20px;
  background-color: #fdafd0;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
  z-index: 10;
}

#storeMemo{
  position: absolute;
  top:570px;
  left: 30px;
}

label {
  display: block;
  width: 100%;
  font-size: 12px;
  line-height: 16px;
}
input {
  width: 300px;
  height: 50px;
  font-size: 2rem;
  padding-left: 20px;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
input:focus,
input:hover,
input:active {
  outline: none;
  box-shadow: none;
  border-color: #f3c0d8;
}
button {
  width: 100px;
  height: 40px;
  font-size: 1.3rem;
  text-align: center;
  border-style: none;
  border-radius: 40px;
  cursor: pointer;
}
#delete {
  position: absolute;
  bottom: 30px;
  right: 200px;
  background-color: rgb(156, 4, 4);
}
#save {
  position: absolute;
  bottom: 30px;
  right: 75px;
  background-color: #26833d;
}
</style>