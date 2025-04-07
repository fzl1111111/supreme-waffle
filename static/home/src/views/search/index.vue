<template>
  <div class="page_search search_index">
	<div class="warp">
	  <div class="container">
		<div class="row">
		  <div class="col-12">
			<div class="card_result_search">
			  <div class="title">搜索结果</div>
				<!-- 商品搜索结果 -->
			  <list_result_search
				:list="result_goods"
				title="电器商城"
				source_table="goods"
			  ></list_result_search>



						  <list_result_search
				v-if="$check_action('/regular_users/list', 'get')"
				:list="result_regular_users_user_name"
				title="普通用户用户姓名"
				source_table="regular_users"
			  ></list_result_search>
								  <list_result_search
				v-if="$check_action('/regular_users/list', 'get')"
				:list="result_regular_users_user_gender"
				title="普通用户用户性别"
				source_table="regular_users"
			  ></list_result_search>
												  <list_result_search
				v-if="$check_action('/digital_mall/list', 'get')"
				:list="result_digital_mall_product_number"
				title="电器商城商品编号"
				source_table="digital_mall"
			  ></list_result_search>
						</div>
		  </div>
		</div>
	  </div>
	</div>
  </div>
</template>

<script>
import mixin from "../../mixins/page.js";
import list_result_search from "../../components/diy/list_result_search.vue";

export default {
  mixins: [mixin],
  data() {
	return {
	  "query": {
		word: "",
	  },
	  "result_goods": [],
						"result_regular_users_user_name":[],
								"result_regular_users_user_gender":[],
												"result_digital_mall_product_number":[],
				};
  },
  methods: {
	/**
	 * 获取${fmodel.filter.cart_name}
	 */
	get_goods() {
	  this.$get("~/api/goods/get_list?like=0", { page: 1, size: 10, title: this.query.word }, (json) => {
		if (json.result) {
		  this.result_goods = json.result.list;
		}
	  });
	},

				/**
	 * 获取user_name
	 */
	get_regular_users_user_name(){
		let url = "~/api/regular_users/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "user_name": this.query.word }, (json) => {
		  if (json.result) {
			var result_regular_users_user_name = json.result.list;
			result_regular_users_user_name.map(o => o.title = o['user_name'])
	  			this.result_regular_users_user_name = result_regular_users_user_name
		 	}
		});
	},
						/**
	 * 获取user_gender
	 */
	get_regular_users_user_gender(){
		let url = "~/api/regular_users/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "user_gender": this.query.word }, (json) => {
		  if (json.result) {
			var result_regular_users_user_gender = json.result.list;
			result_regular_users_user_gender.map(o => o.title = o['user_gender'])
	  			this.result_regular_users_user_gender = result_regular_users_user_gender
		 	}
		});
	},
										/**
	 * 获取product_number
	 */
	get_digital_mall_product_number(){
		let url = "~/api/digital_mall/get_list?like=0";
				this.$get(url, { page: 1, size: 10, "product_number": this.query.word }, (json) => {
		  if (json.result) {
			var result_digital_mall_product_number = json.result.list;
			result_digital_mall_product_number.map(o => o.title = o['product_number'])
	  			this.result_digital_mall_product_number = result_digital_mall_product_number
		 	}
		});
	},
			
  },
  components: { list_result_search },
	created(){
    this.query.word = this.$route.query.word || "";
  },
  mounted() {
	this.get_goods();
					this.get_regular_users_user_name();
							this.get_regular_users_user_gender();
											this.get_digital_mall_product_number();
			  },
  watch: {
	$route() {
	  $.push(this.query, this.$route.query);
	  this.get_goods();
				  this.get_regular_users_user_name();
						  this.get_regular_users_user_gender();
										  this.get_digital_mall_product_number();
				},
  },
};
</script>

<style scoped>
.card_search {
  text-align: center;
}
.card_result_search>.title {
  text-align: center;
  padding: 10px 0;
}
</style>
