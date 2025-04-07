<template>
	<el-form ref="form" :rules="rules" :model="form" status-icon label-width="80px">
			<el-col :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
			<el-form-item label="商品编号" prop="product_number">
						<el-input id="product_number" v-model="form['product_number']" placeholder="请输入商品编号"
					v-if="user_group == '管理员' || (form['digital_mall_id'] && $check_field('set','product_number') ) || $check_field('add','product_number')"></el-input>
				<div v-else-if="$check_field('get','product_number')">{{form['product_number']}}</div>
					</el-form-item>
		</el-col>
	
		<el-col :xs="24" :sm="12" :lg="8" class="el_form_item_warp">
			<el-form-item label="点击数" prop="hits">
				<el-input-number id="hits" v-model="form['hits']"
					v-if="user_group == '管理员' || $check_field('set','hits')"></el-input-number>
				<div v-else-if="$check_field('get','hits')">{{form["hits"]}}</div>
			</el-form-item>
		</el-col>


		<el-col :xs="24" :sm="24" :lg="24" style="text-align: center;" class="el_form_btn_warp">
			<el-button type="primary" @click="submit()">提交</el-button>
			<el-button @click="cancel()">取消</el-button>
		</el-col>

	</el-form>
</template>

<script>
	import mixin from "../../mixins/component.js";

	export default {
		mixins: [mixin],
		props:{
			query: {
				type: Object,
				default: function(){
					return {
						"digital_mall_id": 0
					}
				}
			},
			form_goods:{
				type: Object,
				default: function(){
					return {}
				}
			},
			func_check:{
				type: Function,
				default: function(fun){
					console.log("调试输出",fun);
				}
			},
			func_submit:{
				type: Function,
				default: function(fun){
					console.log("调试输出",fun);
				}
			}
		},
		data() {
			return {
				field: "digital_mall_id",
				url_add: "~/api/digital_mall/add?",
				url_set: "~/api/digital_mall/set?",
				url_get_obj: "~/api/digital_mall/get_obj?",
				url_upload: "~/api/digital_mall/upload?",

				form: {
						"product_number":  '',
						"hits": 0,
				},

	
				rules: {
					"product_number": [     {required: true,message: '商品编号不能为空'},  ],
				}

			}
		},
		methods: {


	
	
	
			submit(){
				this.func_check(()=>{
					this.$refs["form"].validate((valid)} => {
						if (valid) {
							this.submit();
						} else {
							console.error('error 提交失败!!');
						}
					});
				})
			},

			submit_after(){
				var source_id = this.form_goods.source_id;
				if(source_id){
					this.func_submit();
				}else{
					this.$get('~/api/digital_mall/get_obj?',this.form,(res)=>{
						if(res.result && res.result.obj){
							this.form_goods.source_id = res.result.obj["digital_mall_id"];
							this.func_submit();
						}else{
							console.error(res.error);
						}

					})
				}
			}
		},
		created() {
			}
	}
</script>

<style>
	.avatar-uploader .el-upload {
		border: 1px dashed #d9d9d9;
		border-radius: 6px;
		cursor: pointer;
		position: relative;
		overflow: hidden;
	}

	.avatar-uploader .el-upload:hover {
		border-color: #e05d44;
	}

	.avatar-uploader-icon {
		font-size: 28px;
		color: #8c939d;
		width: 178px;
		height: 178px;
		line-height: 178px;
		text-align: center;
	}

	.avatar {
		width: 178px;
		height: 178px;
		display: block;
	}
</style>
