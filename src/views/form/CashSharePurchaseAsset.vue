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
        <basic-table table-name="cash_payment_earnest_money" :pdf-id="pdfId" title="现金+股份购买资产-支付现金-定金"></basic-table>
        <basic-table table-name="payment_cash_payment" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-现金支付"></basic-table>
        <basic-table table-name="stock_purchase_arrangement_in_secondary_market_after_payment" :pdf-id="pdfId" title="现金+股份购买资产-支付现金—支付后二级市场购买股票安排"></basic-table>
        <basic-table table-name="payment_issue_share" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行股份"></basic-table>
        <basic-table table-name="payment_issue_share_share_price_adjustment" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行股份-发行股份价格调整"></basic-table>
        <basic-table table-name="payment_directional_convertible_bonds_issuance" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行定向可转债"></basic-table>
        <basic-form table-name="payment_bonds_convertible_price_downward_revision" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行可转债-转股价格向下修正"></basic-form>
        <basic-form table-name="payment_bonds_conversion_price_upward_modification" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行可转债-转股价格向上修正"></basic-form>
        <basic-form table-name="payment_bonds_early_resale" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行可转债-提前回售"></basic-form>
        <basic-form table-name="payment_bonds_compulsory_equity_swap" :pdf-id="pdfId" title="现金+股份购买资产-支付方式-发行可转债-强制转股"></basic-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import BasicForm from '../../components/Form/BasicForm'
  import BasicTable from '../../components/Form/BasicTable'
  import PDFObject from 'pdfobject'

  export default {
    name: 'CashSharePurchaseAsset',
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
