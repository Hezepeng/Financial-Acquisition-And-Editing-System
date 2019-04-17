<template>
  <div>
    <el-row id="area" :gutter="10" style="margin:30px 10px 10px 15px;">
      <el-col :span="11">
        <el-card :body-style="{ padding: '5px' }">
          <div style="padding: 5px">
            当前编辑的文件名：
            <span style="color: #409EFF">
            {{this.editPdfName}}
            </span>
          </div>
        </el-card>
        <div style="height: 10px"></div>
        <el-card :body-style="{ padding: '0px' }">
          <div v-show="showPdf">
            <div ref="pdfviewer" class="pdfobject-container"></div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="13" style="height:800px;overflow-y: scroll;" v-if="pdfId">
        <basic-table table-name="basic_plan_essential_information" :pdf-id="pdfId" title="基本方案-基本方案-基本信息"></basic-table>
        <basic-form table-name="basic_plan_transaction_type" :pdf-id="pdfId" title="基本方案-基本方案-交易类型"></basic-form>
        <basic-form table-name="basic_plan_payment" :pdf-id="pdfId" title="基本方案-基本方案-支付方式"></basic-form>
        <basic-table table-name="basic_plan_assets_delivery_limited_company" :pdf-id="pdfId" title="基本方案-基本方案-标的资产交割-有限公司"></basic-table>
        <basic-table table-name="basic_plan_assets_delivery_limited_company_listed_companies" :pdf-id="pdfId" title="基本方案-基本方案-标的资产交割-股份有限公司-已挂牌公司"></basic-table>
        <basic-table table-name="basic_plan_assets_delivery_limited_company_unlisted_companies" :pdf-id="pdfId" title="基本方案-基本方案-标的资产交割-股份有限公司-未挂牌公司"></basic-table>
        <basic-form table-name="basic_plan_transition_arrangement" :pdf-id="pdfId" title="基本方案-基本方案-过渡期安排"></basic-form>
        <basic-table table-name="basic_plan_contingent_liability" :pdf-id="pdfId" title="基本方案-基本方案-或有负债"></basic-table>
        <basic-table table-name="basic_plan_integration_corporate_governance_arrangements" :pdf-id="pdfId" title="基本方案-基本方案-交易完成后的整合-公司治理安排"></basic-table>
        <basic-table table-name="integration_labor_relations" :pdf-id="pdfId" title="基本方案-交易完成后的整合-劳动关系"></basic-table>
        <basic-table table-name="integration_financing_support" :pdf-id="pdfId" title="基本方案-交易完成后的整合-融资支持"></basic-table>
        <basic-table table-name="integration_fiscal_taxation_arrangements" :pdf-id="pdfId" title="基本方案-交易完成后的整合-财税安排"></basic-table>
        <basic-table table-name="underlying_assets_transaction_price_adjustment" :pdf-id="pdfId" title="基本方案-标的资产交易价格的调整"></basic-table>
        <basic-table table-name="share_lock_in_period" :pdf-id="pdfId" title="基本方案-股份锁定期"></basic-table>
        <basic-table table-name="residual_stocks_in_underlying_assets_arrangement" :pdf-id="pdfId" title="基本方案-标的资产剩余股权的安排"></basic-table>
        <basic-table table-name="breach_contract_liability" :pdf-id="pdfId" title="基本方案-违约责任"></basic-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import BasicForm from '../../components/Form/BasicForm'
  import BasicTable from '../../components/Form/BasicTable'
  import PDFObject from 'pdfobject'

  export default {
    name: 'BasicPlan',
    components: { BasicTable, BasicForm },

    data() {
      return {
        screenHeight: document.documentElement.clientHeight,
        showPdf: true
      }
    },
    computed: {
      pdfId: function() {
        return this.$store.state.app.editPdfId
      },
      editPdfName: function() {
        return this.$store.state.app.editPdfName
      },
      documentOriginLocation: function() {
        return '/src/pdf/' + this.$store.state.app.editPdfName
      }
    },
    mounted() {
      if (!this.pdfId) {
        this.$alert('请先选择要编辑的文件', '温馨提示', {
          confirmButtonText: '去选择文件',
          center: true,
          callback: action => {
            this.$router.push({ name: 'pdfList' })
          }
        })
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
</style>
