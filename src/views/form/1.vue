<template>
  <div>
    <el-row id="area" :gutter="10" style="margin:30px 10px 10px 15px;">
      <el-col :span="11">
        <el-card :body-style="{ padding: '0px' }">
          <div v-show="showPdf">
            <div ref="pdfviewer" class="pdfobject-container"/>
          </div>
        </el-card>
      </el-col>

      <el-col :span="13" style="height:800px;overflow-y: scroll;">

        <!--基本信息-->
        <el-card>
          <span class="card-title">基本信息</span>
          <el-form ref="form" :model="form" label-width="140px">
            <el-form-item label="上市公司简称">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="上市地点">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="上市公司证券代码">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="上市公司所属行业">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="上市公司主营业务">
              <el-input v-model="form.name" type="textarea"/>
            </el-form-item>
            <el-form-item label="标的公司">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="交易资产所占标的公司的股权比例">
              <el-input v-model="form.desc"/>
            </el-form-item>
            <el-form-item label="标的公司所属行业">
              <el-input v-model="form.desc" type="textarea"/>
            </el-form-item>
            <el-form-item label="标的公司主营业务">
              <el-input v-model="form.desc" type="textarea"/>
            </el-form-item>
            <el-form-item label="滚存未分配利润归属">
              <el-input v-model="form.desc" type="textarea"/>
            </el-form-item>
            <el-form-item label="交易价格（万元）">
              <el-input v-model="form.desc"/>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">保存</el-button>
              <el-button @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易类型-->
        <el-card>
          <span class="card-title">交易类型</span>
          <el-form ref="form" :model="form">
            <el-form-item>
              <el-checkbox-group v-model="form.type">
                <el-checkbox label="是否构成重大资产重组" name="type"/>
                <el-checkbox label="是否为关联交易" name="type"/>
                <el-checkbox label="是否够成上市公司控制权变化" name="type"/>
                <el-checkbox label="资产置换" name="type"/>
                <el-checkbox label="现金购买资产" name="type"/>
                <el-checkbox label="发行股份购买资产" name="type"/>
                <el-checkbox label="出售资产" name="type"/>
                <el-checkbox label="吸收合并" name="type"/>
                <el-checkbox label="分立" name="type"/>
                <el-checkbox label="上市公司收购" name="type"/>
                <el-checkbox label="要约收购" name="type"/>
                <el-checkbox label="是否募集配套资金" name="type"/>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">保存</el-button>
              <el-button @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
        </el-card>
        <div style="height: 30px;"/>

        <!--支付方式-->
        <el-card>
          <span class="card-title">支付方式</span>
          <el-form ref="form" :model="form">
            <el-form-item>
              <el-checkbox-group v-model="form.type">
                <el-checkbox label="现金" name="type"/>
                <el-checkbox label="现金比例" name="type"/>
                <el-checkbox label="股份" name="type"/>
                <el-checkbox label="股份比例" name="type"/>
                <el-checkbox label="定向可转债" name="type"/>
                <el-checkbox label="定向可转债比例" name="type"/>
              </el-checkbox-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">保存</el-button>
              <el-button @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
        </el-card>
        <div style="height: 30px;"/>

        <!--标的资产交割-有限公司-->
        <el-card>
          <span class="card-title">标的资产交割-有限公司</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="标的资产名称"/>
            <el-table-column
              prop="name"
              label="董事、监事、高级管理人员股权交割时间"/>
            <el-table-column
              prop="address"
              label="控股股东及实际控制人股权交割时间"/>
            <el-table-column
              prop="address"
              label="其他股东股权交割时间"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--标的资产交割-股份有限公司-->
        <el-card>
          <span class="card-title">标的资产交割-股份有限公司</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="标的资产名称"/>
            <el-table-column
              prop="name"
              label="挂牌地点"/>
            <el-table-column
              prop="address"
              label="是否终止挂牌"/>
            <el-table-column
              prop="address"
              label="摘牌时间"/>
            <el-table-column
              prop="address"
              label="变更为有限公司时间"/>
            <el-table-column
              prop="address"
              label="董事、监事、高级管理人员股权过户时间"/>
            <el-table-column
              prop="address"
              label="是其他股东股权过户时间否终止挂牌"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--过渡期-->
        <el-card>
          <span class="card-title">过渡期</span>
          <el-form ref="form" :model="form" label-width="140px">
            <el-form-item label="过渡期时间">
              <el-input v-model="form.name" type="textarea"/>
            </el-form-item>
            <el-form-item label="过渡期内标的公司是否分红">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="分红方式">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="过渡期盈利归属">
              <el-input v-model="form.name" type="textarea"/>
            </el-form-item>
            <el-form-item label="过渡期损失归属">
              <el-input v-model="form.name" type="textarea"/>
            </el-form-item>
            <el-form-item label="过渡期损失是否按比例承担">
              <el-input v-model="form.name" type="textarea"/>
            </el-form-item>
            <el-form-item label="过渡期损失是否连带承担责任">
              <el-input v-model="form.name"/>
            </el-form-item>
            <el-form-item label="过渡期损益的审计时间">
              <el-input v-model="form.desc" type="textarea"/>
            </el-form-item>
            <el-form-item label="过渡期其他安排">
              <el-input v-model="form.desc" type="textarea"/>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">保存</el-button>
              <el-button @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
        </el-card>
        <div style="height: 30px;"/>

        <!--或有负债-->
        <el-card>
          <span class="card-title">或有负债</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="债务范围"/>
            <el-table-column
              prop="name"
              label="承担主体"/>
            <el-table-column
              prop="address"
              label="是否按比例承担"/>
            <el-table-column
              prop="address"
              label="是否承担连带责任"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易完成后的整合-经营安排-->
        <el-card>
          <span class="card-title">交易完成后的整合-经营安排</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="各项经营安排安排"/>
            <el-table-column
              prop="name"
              label="重大事项"/>
            <el-table-column
              prop="address"
              label="同业竞争"/>
            <el-table-column
              prop="address"
              label="是否承担连带责任"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易完成后的整合-公司治理安排-->
        <el-card>
          <span class="card-title">交易完成后的整合-公司治理安排</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="董事会构成"/>
            <el-table-column
              prop="name"
              label="监事会构成"/>
            <el-table-column
              prop="address"
              label="法定代表人"/>
            <el-table-column
              prop="address"
              label="董事长"/>
            <el-table-column
              prop="address"
              label="董事会决议程序"/>
            <el-table-column
              prop="address"
              label="高级管理人员"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易完成后的整合-劳动关系-->
        <el-card>
          <span class="card-title">交易完成后的整合-劳动关系</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="主体"/>
            <el-table-column
              prop="name"
              label="身份"/>
            <el-table-column
              prop="address"
              label="劳动合同期限"/>
            <el-table-column
              prop="address"
              label="竞业禁止开始时间"/>
            <el-table-column
              prop="address"
              label="竞业禁止结束时间"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易完成后的整合-融资支持-->
        <el-card>
          <span class="card-title">交易完成后的整合-融资支持</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="借款"/>
            <el-table-column
              prop="name"
              label="增资"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--交易完成后的整合-财务安排-->
        <el-card>
          <span class="card-title">交易完成后的整合-财务安排</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="财务"/>
            <el-table-column
              prop="name"
              label="税务"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--标的资产交易价格的调整（云投生态）-->
        <el-card>
          <span class="card-title">标的资产交易价格的调整（云投生态）</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="支付对方"/>
            <el-table-column
              prop="name"
              label="触发条件"/>
            <el-table-column
              prop="date"
              label="调整后的交易价格（万元）"/>
            <el-table-column
              prop="name"
              label="调整后的交易价格确定时间"/>
            <el-table-column
              prop="date"
              label="调整后交易价格增加额（万元）"/>
            <el-table-column
              prop="name"
              label="调整后的交易价格支付时间"/>
            <el-table-column
              prop="date"
              label="现金支付"/>
            <el-table-column
              prop="name"
              label="股份支付"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--股份锁定期-->
        <el-card>
          <span class="card-title">股份锁定期</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="锁定主体"/>
            <el-table-column
              prop="name"
              label="身份"/>
            <el-table-column
              prop="date"
              label="锁定期限"/>
            <el-table-column
              prop="name"
              label="锁定期内新增可转让股份数（股）"/>
            <el-table-column
              prop="date"
              label="锁定期内新增可转让股份所占比例（%）"/>
            <el-table-column
              prop="name"
              label="锁定期延长"/>
            <el-table-column
              prop="date"
              label="是否存在补偿义务扣减股份数"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--标的资产剩余股权的安排-->
        <el-card>
          <span class="card-title">标的资产剩余股权的安排</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="剩余股权股东名称"/>
            <el-table-column
              prop="name"
              label="持股数量"/>
            <el-table-column
              prop="name"
              label="持股比例"/>
            <el-table-column
              prop="name"
              label="后续安排"/>
            <el-table-column
              prop="name"
              label="时间安排"/>
            <el-table-column
              prop="name"
              label="交易作价"/>
            <el-table-column
              prop="name"
              label="支付方式"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--支付后二级市场购买股票安排-->
        <el-card>
          <span class="card-title">支付后二级市场购买股票安排</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="购买主体"/>
            <el-table-column
              prop="name"
              label="购买时间"/>
            <el-table-column
              prop="name"
              label="购买数额"/>
            <el-table-column
              prop="name"
              label="购买方式"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>

        <!--违约责任-->
        <el-card>
          <span class="card-title">违约责任</span>
          <el-table
            :data="tableData"
            border
            style="width: 100%;margin-top: 20px">
            <el-table-column
              prop="date"
              label="违约主体"/>
            <el-table-column
              prop="name"
              label="违约行为"/>
            <el-table-column
              prop="name"
              label="违约金计算方式"/>
            <el-table-column
              prop="name"
              label="各主体是否承担连带责任"/>
          </el-table>
          <div style="margin-top: 20px">
            <el-button type="primary" @click="onSubmit">保存</el-button>
            <el-button @click="onCancel">取消</el-button>
          </div>
        </el-card>
        <div style="height: 30px;"/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import PDFObject from 'pdfobject'

  export default {
    name: '1',
    data() {
      return {
        documentObj: {},
        checkStatus: '',
        documentOriginLocation: '/src/pdf/丽鹏股份：发行股份及支付现金购买资产并募集配套资金暨关联交易报告书（修订稿） (1).pdf',
        screenHeight: document.documentElement.clientHeight,
        ifDelete: 'save',
        docText: '',
        docRight: true,
        docLeft: false,
        difList: [],
        showPdf: true,
        toPage: {},
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市'
        }]
      }
    },
    watch: {
      toPage: {
        handler: function(val, oldVal) {
          this.$nextTick(function() {
            const pdfnode = this.$refs.pdfviewer
            // const pdfnodeleft = this.$refs.pdfviewerleft
            PDFObject.embed(this.documentOriginLocation, pdfnode, val)
            // PDFObject.embed(this.documentOriginLocation, pdfnodeleft, val)
          })
        },
        deep: true,
        immediate: true
      }
    }
  }

</script>

<style scoped>
  .pdfobject-container {
    height: 800px;
    width: 100%;
    display: block;
    margin: auto;
  }

  .pdfobject {
    border: 1px solid #666;
  }

  .card-title {
    font-size: 18px;
  }
</style>
