from django.contrib.postgres.fields import ArrayField
from django.db import models


# PDF文件列表-table
class pdf_information(models.Model):
  class Meta:
    db_table = "pdf_information"

  pdf_id = models.TextField(primary_key=True)
  create_time = models.DateField(blank=True, null=True)
  simple_name = models.TextField(blank=False, null=False)
  full_name = models.TextField(blank=False, null=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 标的公司组合-table
class target_company_package(models.Model):
  class Meta:
    db_table = "target_company_package"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=True, default=None)
  create_time = models.DateField(blank=True, null=True)
  module_name = models.TextField(blank=False, null=False)
  package_name = models.TextField(blank=False, null=False)
  company_id_list = ArrayField(models.IntegerField(blank=False, null=False))

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 标的公司在组合中是否使用过-table
class target_company_used_in_package(models.Model):
  class Meta:
    db_table = "target_company_used_in_package"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=True, default=None)
  company = models.ForeignKey("basic_plan_essential_information", on_delete=models.CASCADE, null=True, default=None)
  module_name = models.TextField(blank=False, null=False)
  used_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-基本信息-table
class basic_plan_essential_information(models.Model):
  class Meta:
    db_table = "basic_plan_essential_information"

  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  used_flag = models.BooleanField(blank=False, null=False, default=False)
  row_id = models.AutoField(primary_key=True)
  listed_companies_abbreviation = models.TextField(blank=True, null=True)
  listing_place = models.TextField(blank=True, null=True)
  listed_companies_securities_code = models.TextField(blank=True, null=True)
  listed_companies = models.TextField(blank=True, null=True)
  listed_companies_main_business = models.TextField(blank=True, null=True)
  target_company = models.TextField(blank=True, null=True)
  transacted_assets_to_target_company_stock_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  target_company_inc = models.TextField(blank=True, null=True)
  target_company_main_business = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-交易类型-form
class basic_plan_transaction_type(models.Model):
  class Meta:
    db_table = "basic_plan_transaction_type"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  constituting_major_asset_restructuring_flag = models.BooleanField(blank=False, null=False, default=False)
  for_affiliated_transactions_flag = models.BooleanField(blank=False, null=False, default=False)
  listed_companies_enough_to_change_control_rights_flag = models.BooleanField(blank=False, null=False, default=False)
  asset_replacement_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_purchase_assets_flag = models.BooleanField(blank=False, null=False, default=False)
  issuing_share_to_purchase_assets_flag = models.BooleanField(blank=False, null=False, default=False)
  assets_sale_flag = models.BooleanField(blank=False, null=False, default=False)
  absorption_merger_flag = models.BooleanField(blank=False, null=False, default=False)
  discrete_flag = models.BooleanField(blank=False, null=False, default=False)
  listed_companies_acquisition_flag = models.BooleanField(blank=False, null=False, default=False)
  tender_offer_flag = models.BooleanField(blank=False, null=False, default=False)
  raising_matching_funds_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-支付方式-form
class basic_plan_payment(models.Model):
  class Meta:
    db_table = "basic_plan_payment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  cash_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_ratio = models.TextField(blank=True, null=True)
  share_flag = models.BooleanField(blank=False, null=False, default=False)
  share_ratio = models.TextField(blank=True, null=True)
  convertible_bonds_flag = models.BooleanField(blank=False, null=False, default=False)
  convertible_bond_ratio = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-标的资产交割-有限公司-table
class basic_plan_assets_delivery_limited_company(models.Model):
  class Meta:
    db_table = "basic_plan_assets_delivery_limited_company"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  underlying_assets_name = models.TextField(blank=True, null=True)
  director_supervisor_seniorstock_delivery_time = models.TextField(blank=True, null=True)
  shareholder_controller_stock_delivery_time = models.TextField(blank=True, null=True)
  other_shareholders_tock_delivery_times = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-标的资产交割-股份有限公司-已挂牌公司-table
class basic_plan_assets_delivery_limited_company_listed_companies(models.Model):
  class Meta:
    db_table = "basic_plan_assets_delivery_limited_company_listed_companies"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  underlying_assets_name = models.TextField(blank=True, null=True)
  share_company_setup_time = models.DateField(blank=True, null=True)
  listing_place = models.TextField(blank=True, null=True)
  listing_time = models.DateField(blank=True, null=True)
  shareholder_limitation_arrangement = models.TextField(blank=True, null=True)
  listing_termination_flag = models.BooleanField(blank=False, null=False, default=False)
  delisting_time = models.TextField(blank=True, null=True)
  change_share_company_to_limited_company_time = models.TextField(blank=True, null=True)
  shareholder_controller_stock_delivery_time = models.TextField(blank=True, null=True)
  director_supervisor_seniorstock_transfer_time = models.TextField(blank=True, null=True)
  other_shareholders_tock_transfer_times = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-标的资产交割-股份有限公司-未挂牌公司-table
class basic_plan_assets_delivery_limited_company_unlisted_companies(models.Model):
  class Meta:
    db_table = "basic_plan_assets_delivery_limited_company_unlisted_companies"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  underlying_assets_name = models.TextField(blank=True, null=True)
  share_company_setup_time = models.DateField(blank=True, null=True)
  shareholder_limitation_arrangement = models.TextField(blank=True, null=True)
  change_share_company_to_limited_company_time = models.TextField(blank=True, null=True)
  shareholder_controller_stock_delivery_time = models.TextField(blank=True, null=True)
  director_supervisor_seniorstock_transfer_time = models.TextField(blank=True, null=True)
  other_shareholders_tock_transfer_times = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-过渡期安排-form
class basic_plan_transition_arrangement(models.Model):
  class Meta:
    db_table = "basic_plan_transition_arrangement"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  transition_time = models.TextField(blank=True, null=True)
  target_company_dividend_in_transition_flag = models.BooleanField(blank=False, null=False, default=False)
  bonus_method = models.TextField(blank=True, null=True)
  transition_profit_attribution = models.TextField(blank=True, null=True)
  transition_loss_attribution = models.TextField(blank=True, null=True)
  transition_losses_are_borne_proportionally_flag = models.BooleanField(blank=False, null=False, default=False)
  transition_losses_joint_several_liability_flag = models.BooleanField(blank=False, null=False, default=False)
  transition_gains_losses_audit_time = models.TextField(blank=True, null=True)
  other_transition_arrangements = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-或有负债-table
class basic_plan_contingent_liability(models.Model):
  class Meta:
    db_table = "basic_plan_contingent_liability"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  debt_scope = models.TextField(blank=True, null=True)
  subject_name = models.TextField(blank=True, null=True)
  subject_identity = models.TextField(blank=True, null=True)
  prorated_commitment_flag = models.BooleanField(blank=False, null=False, default=False)
  joint_several_liability_flag = models.BooleanField(blank=False, null=False, default=False)
  joint_several_liability_subject = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 基本方案-交易完成后的整合-公司治理安排-table
class basic_plan_integration_corporate_governance_arrangements(models.Model):
  class Meta:
    db_table = "basic_plan_integration_corporate_governance_arrangements"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  board_of_directors_composition = models.TextField(blank=True, null=True)
  board_of_supervisors_composition = models.TextField(blank=True, null=True)
  legal_representative = models.TextField(blank=True, null=True)
  chairman = models.TextField(blank=True, null=True)
  board_resolution_procedure = models.TextField(blank=True, null=True)
  resolution_major_matters_procedures = models.TextField(blank=True, null=True)
  senior = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 交易完成后的整合-劳动关系-table
class integration_labor_relations(models.Model):
  class Meta:
    db_table = "integration_labor_relations"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  subject = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  labor_contract_term = models.TextField(blank=True, null=True)
  prohibition_of_competition_term = models.TextField(blank=True, null=True)
  non_competition_starting_time = models.TextField(blank=True, null=True)
  non_competition_ending_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 交易完成后的整合-融资支持-table
class integration_financing_support(models.Model):
  class Meta:
    db_table = "integration_financing_support"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  support_mode = models.TextField(blank=True, null=True)
  support_amount = models.TextField(blank=True, null=True)
  support_conditions = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 交易完成后的整合-财税安排-table
class integration_fiscal_taxation_arrangements(models.Model):
  class Meta:
    db_table = "integration_fiscal_taxation_arrangements"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  finance = models.TextField(blank=True, null=True)
  taxation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 标的资产交易价格的调整-table
class underlying_assets_transaction_price_adjustment(models.Model):
  class Meta:
    db_table = "underlying_assets_transaction_price_adjustment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  payment_object = models.TextField(blank=True, null=True)
  payment_object_identity = models.TextField(blank=True, null=True)
  trigger_condition = models.TextField(blank=True, null=True)
  underlying_assets_before_adjustment_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  adjusted_underlying_assets_transaction_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  adjusted_underlying_assets_transaction_price_increase = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  adjusted_trading_price_determination_time = models.TextField(blank=True, null=True)
  adjusted_transaction_amount_payment_time = models.TextField(blank=True, null=True)
  cash_payment_amount = models.TextField(blank=True, null=True)
  share_payment_amount = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 股份锁定期-table
class share_lock_in_period(models.Model):
  class Meta:
    db_table = "share_lock_in_period"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  share_locks_subject = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  share_lock_in_period = models.TextField(blank=True, null=True)
  new_transferable_share_number_during_lock_in_period = models.TextField(blank=True, null=True)
  new_transferable_share_in_lock_in_period_proportion = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  prolonged_locking_period = models.TextField(blank=True, null=True)
  share_deduction_with_compensation_obligation_flag = models.BooleanField(blank=False, null=False, default=False)
  new_share_listing_time = models.TextField(blank=True, null=True)
  limited_shareto_sale_circulation_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 标的资产剩余股权的安排-table
class residual_stocks_in_underlying_assets_arrangement(models.Model):
  class Meta:
    db_table = "residual_stocks_in_underlying_assets_arrangement"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  shareholder_holding_underlying_assets_remaining_stock = models.TextField(blank=True, null=True)
  shareholding_quantity = models.TextField(blank=True, null=True)
  shareholding_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  residual_stock_follow_up_arrangement = models.TextField(blank=True, null=True)
  remaining_stock_acquisition_time_arrangement = models.TextField(blank=True, null=True)
  transaction_pricing = models.TextField(blank=True, null=True)
  payment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 违约责任-table
class breach_contract_liability(models.Model):
  class Meta:
    db_table = "breach_contract_liability"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  breach_of_contract_subject = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  contract_breach = models.TextField(blank=True, null=True)
  default_type = models.TextField(blank=True, null=True)
  liquidated_damages_calculating_method = models.TextField(blank=True, null=True)
  each_subject_joint_several_liabilities_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付现金-定金-table
class cash_payment_earnest_money(models.Model):
  class Meta:
    db_table = "cash_payment_earnest_money"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  payment_object = models.TextField(blank=True, null=True)
  payment_object_identity = models.TextField(blank=True, null=True)
  deposit_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  deposit_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  payment_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-现金支付-table
class payment_cash_payment(models.Model):
  class Meta:
    db_table = "payment_cash_payment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  counterparty_name = models.TextField(blank=True, null=True)
  counterparty_identity = models.TextField(blank=True, null=True)
  cash_payment_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  first_stage_payment_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  first_payment_period = models.TextField(blank=True, null=True)
  payment_in_second_instalment_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_payment_period = models.TextField(blank=True, null=True)
  payment_in_third_instalment_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_payment_period = models.TextField(blank=True, null=True)
  one_time_cash_payment_time = models.TextField(blank=True, null=True)
  compensation_or_amount_of_compensation_deduction_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付现金—支付后二级市场购买股票安排-table
class stock_purchase_arrangement_in_secondary_market_after_payment(models.Model):
  class Meta:
    db_table = "stock_purchase_arrangement_in_secondary_market_after_payment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  buying_body = models.TextField(blank=True, null=True)
  purchaser_identity = models.TextField(blank=True, null=True)
  buying_time = models.TextField(blank=True, null=True)
  purchase_amount = models.TextField(blank=True, null=True)
  purchasing_ways = models.TextField(blank=True, null=True)
  purchase_share_lock_in_period_arrangement = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行股份-table
class payment_issue_share(models.Model):
  class Meta:
    db_table = "payment_issue_share"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  issue_object = models.TextField(blank=True, null=True)
  issuer_identity = models.TextField(blank=True, null=True)
  transaction_amount_purchased_by_issuing_share = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  issue_quantity = models.TextField(blank=True, null=True)
  pricing_date = models.TextField(blank=True, null=True)
  issue_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行股份-发行股份价格调整-table
class payment_issue_share_share_price_adjustment(models.Model):
  class Meta:
    db_table = "payment_issue_share_share_price_adjustment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  trigger_condition_type = models.TextField(blank=True, null=True)
  trigger_condition_content = models.TextField(blank=True, null=True)
  price_adjustment_date = models.TextField(blank=True, null=True)
  adjustable_price_period = models.TextField(blank=True, null=True)
  price_adjustment_mechanism = models.TextField(blank=True, null=True)
  pre_adjustment_issue_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  adjusted_issue_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行定向可转债-table
class payment_directional_convertible_bonds_issuance(models.Model):
  class Meta:
    db_table = "payment_directional_convertible_bonds_issuance"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  issue_object = models.TextField(blank=True, null=True)
  issuer_identity = models.TextField(blank=True, null=True)
  target_companystock_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  bonds_payment_consideration_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  issue_quantity = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  bonds_convertible_quantity_at_initial_conversion_price = models.TextField(blank=True, null=True)
  issuing_mode = models.TextField(blank=True, null=True)
  bond_maturity = models.TextField(blank=True, null=True)
  stock_transfer_period = models.TextField(blank=True, null=True)
  bond_interest_rate = models.TextField(blank=True, null=True)
  interest_bearing_method = models.TextField(blank=True, null=True)
  setting_up_guarantee_flag = models.BooleanField(blank=False, null=False, default=False)
  conversion_price = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行可转债-转股价格向下修正-form
class payment_bonds_convertible_price_downward_revision(models.Model):
  class Meta:
    db_table = "payment_bonds_convertible_price_downward_revision"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  downward_revision_period = models.TextField(blank=True, null=True)
  price_conditions_downward_revision = models.TextField(blank=True, null=True)
  conversion_price_before_downward_amendment = models.TextField(blank=True, null=True)
  downward_modified_price_interval = models.TextField(blank=True, null=True)
  downward_modified_conversion_price = models.TextField(blank=True, null=True)
  downward_revisions_number = models.TextField(blank=True, null=True)
  price_scope_downward_modification = models.TextField(blank=True, null=True)
  downward_revision_procedure = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行可转债-转股价格向上修正-form
class payment_bonds_conversion_price_upward_modification(models.Model):
  class Meta:
    db_table = "payment_bonds_conversion_price_upward_modification"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  upward_revision_period = models.TextField(blank=True, null=True)
  price_conditions_upward_modification = models.TextField(blank=True, null=True)
  conversion_price_before_upward_amendment = models.TextField(blank=True, null=True)
  upward_modified_price_interval = models.TextField(blank=True, null=True)
  upward_modified_conversion_price = models.TextField(blank=True, null=True)
  upward_revision_times = models.TextField(blank=True, null=True)
  price_scope_upward_modification = models.TextField(blank=True, null=True)
  upward_revision_procedure = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行可转债-提前回售-form
class payment_bonds_early_resale(models.Model):
  class Meta:
    db_table = "payment_bonds_early_resale"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  pre_sale_conditions = models.TextField(blank=True, null=True)
  pre_sale_method = models.TextField(blank=True, null=True)
  exercise_period = models.TextField(blank=True, null=True)
  interest_on_unsold_part_calculation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付方式-发行可转债-强制转股-form
class payment_bonds_compulsory_equity_swap(models.Model):
  class Meta:
    db_table = "payment_bonds_compulsory_equity_swap"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  mandatory_equity_swap_conditions = models.TextField(blank=True, null=True)
  compulsory_share_conversion_procedure = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 发行股份及募集配套资金基本概况-table
class issuing_share_raising_matching_funds_basic_situation(models.Model):
  class Meta:
    db_table = "issuing_share_raising_matching_funds_basic_situation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  distribution_object_name = models.TextField(blank=True, null=True)
  issuer_identity = models.TextField(blank=True, null=True)
  raising_matching_funds = models.TextField(blank=True, null=True)
  issue_quantity = models.TextField(blank=True, null=True)
  pricing_date = models.TextField(blank=True, null=True)
  issue_price = models.TextField(blank=True, null=True)
  payment = models.TextField(blank=True, null=True)
  issuing_mode = models.TextField(blank=True, null=True)
  merger_acquisition_bottom_price_matching_financing = models.TextField(blank=True, null=True)
  merger_acquisition_matching_financing_price = models.TextField(blank=True, null=True)
  issuance_price_over_issuance_base_price_floating_rate = models.TextField(blank=True, null=True)
  next_day_sfc_approves_closing_price = models.TextField(blank=True, null=True)
  issuance_price_over_approved_next_day_discount_rate = models.TextField(blank=True, null=True)
  date_of_securities_regulatory_commission_average_daily_price = models.TextField(blank=True, null=True)
  sfc_issuance_price_two0_days_before_approval = models.TextField(blank=True, null=True)
  share_lock_in_period = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 资产评估-基础数据-form
class assets_appraisal_basic_data(models.Model):
  class Meta:
    db_table = "assets_appraisal_basic_data"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  assessment_method = models.TextField(blank=True, null=True)
  assessment_baseline_date = models.DateField(blank=True, null=True)
  supplementary_assessment_baseline_date = models.DateField(blank=True, null=True)
  book_net_assets = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  assessment_results = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  evaluation_increment = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  appreciation_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  applying_methods_to_evaluate_results = models.TextField(blank=True, null=True)
  transaction_price = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  transaction_value_added_rate = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 标的资产的财务数据-form
class underlying_assets_financial_data(models.Model):
  class Meta:
    db_table = "underlying_assets_financial_data"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  reporting_period_first_year = models.TextField(blank=True, null=True)
  first_year_reporting_period_audited_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  reporting_period_second_year = models.TextField(blank=True, null=True)
  year_underlying_assets_reporting_period_audited_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  reporting_period_period_i = models.TextField(blank=True, null=True)
  understanding_assets_reporting_period_audited_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  annual_declaration = models.TextField(blank=True, null=True)
  year_underlying_assets_declare_performance_commitment = models.TextField(blank=True, null=True)
  audited_in_year_before_it_was_declared_performance_commitment = models.TextField(blank=True, null=True)
  first_year_after_declaration = models.TextField(blank=True, null=True)
  performance_commitment_number_in_first_year_after_declaration = models.TextField(blank=True, null=True)
  actually_achieved_in_first_year_after_declaration_number = models.TextField(blank=True, null=True)
  to_commitment_in_first_year_after_declaration_proportion = models.TextField(blank=True, null=True)
  year_two_after_declaration = models.TextField(blank=True, null=True)
  performance_commitment_number_in_second_year_after_declaration = models.TextField(blank=True, null=True)
  actual_achievements_in_second_year_after_declaration = models.TextField(blank=True, null=True)
  to_commitment_in_second_year_after_declaration_ratio = models.TextField(blank=True, null=True)
  year_three_after_declaration = models.TextField(blank=True, null=True)
  annual_performance_commitment_in_third_year_after_declaration = models.TextField(blank=True, null=True)
  actual_achievements_in_third_year_after_declaration = models.TextField(blank=True, null=True)
  to_commitment_in_third_year_after_declaration_ratio = models.TextField(blank=True, null=True)
  fourth_year_after_declaration = models.TextField(blank=True, null=True)
  annual_performance_commitment_in_fourth_year_after_declaration = models.TextField(blank=True, null=True)
  actual_achievements_in_fourth_year_after_declaration = models.TextField(blank=True, null=True)
  to_commitment_in_fourth_year_after_declaration_proportion = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 交易市盈率-form
class trading_pe(models.Model):
  class Meta:
    db_table = "trading_pe"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  year_before_declaration_static_pe_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  annual_declaration = models.TextField(blank=True, null=True)
  declare_current_year_dynamic_pe_ratio = models.TextField(blank=True, null=True)
  year_two_after_declaration = models.TextField(blank=True, null=True)
  dynamic_pe_ratio_in_second_year_after_declaration = models.TextField(blank=True, null=True)
  year_three_after_declaration = models.TextField(blank=True, null=True)
  dynamic_pe_ratio_in_third_year_after_declaration = models.TextField(blank=True, null=True)
  fourth_year_after_declaration = models.TextField(blank=True, null=True)
  dynamic_pe_ratio_in_fourth_year_after_declaration = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-form
class performance_commitment_arrangement(models.Model):
  class Meta:
    db_table = "performance_commitment_arrangement"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  performance_commitment_arrangement_committed_person = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  shareholding_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺期间-form
class performance_commitment_arrangement_commitment_period(models.Model):
  class Meta:
    db_table = "performance_commitment_arrangement_commitment_period"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  committed_person = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  three_years_flag = models.BooleanField(blank=False, null=False, default=False)
  four_years_flag = models.BooleanField(blank=False, null=False, default=False)
  specific_year = models.TextField(blank=True, null=True)
  duration_extension_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-form
class performance_commitment_arrangement_committed_performance(models.Model):
  class Meta:
    db_table = "performance_commitment_arrangement_committed_performance"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  committed_person = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  commitment_to_net_profit_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_net_operating_cash_flow = models.TextField(blank=True, null=True)
  commitment_to_sign_contract_amount = models.TextField(blank=True, null=True)
  committed_inventory_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_accounts_receivable_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_long_term_receivables_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺净利润-table
class arrangement_committed_performance_commitment_to_net_profit(models.Model):
  class Meta:
    db_table = "arrangement_committed_performance_commitment_to_net_profit"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_to_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  accumulated_commitment_net_profit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺经营性现金流量净额-table
class committed_performance_commitment_to_net_operating_cash_flow(models.Model):
  class Meta:
    db_table = "committed_performance_commitment_to_net_operating_cash_flow"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  net_operating_cash_flow_promised_in_first_year = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_net_operating_cash_flow_promised = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_net_operating_cash_flow_promised = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_net_operating_cash_flow_promised = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  accumulated_net_operating_cash_flow_commitment = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺签订合同金额-table
class committed_performance_commitment_to_sign_contract_amount(models.Model):
  class Meta:
    db_table = "committed_performance_commitment_to_sign_contract_amount"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  contract_promised_in_first_year_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  contract_promised_in_second_year_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  contract_promised_in_third_year_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  contract_promised_in_fourth_year_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  accumulative_undertaking_to_sign_contract = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺存货-table
class arrangement_committed_performance_committed_inventory(models.Model):
  class Meta:
    db_table = "arrangement_committed_performance_committed_inventory"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  recovery_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺存货-回收率-table
class committed_performance_committed_inventory_recovery_rate(models.Model):
  class Meta:
    db_table = "committed_performance_committed_inventory_recovery_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_inventory_recovery_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_inventory_recovery_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_inventory_recovery_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_inventory_recovery_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺存货-周转率-table
class committed_performance_committed_inventory_turnover_rate(models.Model):
  class Meta:
    db_table = "committed_performance_committed_inventory_turnover_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_inventory_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_inventory_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_inventory_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_inventory_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺应收账款-table
class committed_performance_commitment_to_accounts_receivable(models.Model):
  class Meta:
    db_table = "committed_performance_commitment_to_accounts_receivable"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  recovery_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺应收账款-回收率-table
class performance_commitment_to_accounts_receivable_recovery_rate(models.Model):
  class Meta:
    db_table = "performance_commitment_to_accounts_receivable_recovery_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_receivables_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_receivables_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_receivables_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_receivables_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺应收账款-周转率-table
class performance_commitment_to_accounts_receivable_turnover_rate(models.Model):
  class Meta:
    db_table = "performance_commitment_to_accounts_receivable_turnover_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_receivables_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_receivable_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_receivable_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_receivable_turnover_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺长期应收款-table
class committed_performance_commitment_to_long_term_receivables(models.Model):
  class Meta:
    db_table = "committed_performance_commitment_to_long_term_receivables"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  recovery_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺长期应收款-回收率-table
class performance_commitment_to_long_term_receivables_recovery_rate(models.Model):
  class Meta:
    db_table = "performance_commitment_to_long_term_receivables_recovery_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commitment_long_term_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commitment_long_term_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commitment_long_term_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commitment_long_term_recovery_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩-承诺长期应收款-周转率-table
class performance_commitment_to_long_term_receivables_turnover_rate(models.Model):
  class Meta:
    db_table = "performance_commitment_to_long_term_receivables_turnover_rate"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_commit_long_term_turnover_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  second_year_commit_long_term_turnover_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_commit_long_term_turnover_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  fourth_years = models.TextField(blank=True, null=True)
  fourth_year_commit_long_term_turnover_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  actual_performance_audit = models.TextField(blank=True, null=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺安排-承诺业绩计算标准-form
class arrangement_commitment_performance_computing_criteria(models.Model):
  class Meta:
    db_table = "arrangement_commitment_performance_computing_criteria"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  deduction_items_type = models.TextField(blank=True, null=True)
  realized_in_current_period_can_be_included_in_next_period = models.TextField(blank=True, null=True)
  financial_statements_basfor_preparation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-form
class performance_forecast_compensation(models.Model):
  class Meta:
    db_table = "performance_forecast_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  stock_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  compensation_period = models.TextField(blank=True, null=True)
  compensation_obligation_triggering_conditions = models.TextField(blank=True, null=True)
  compensation_amount = models.TextField(blank=True, null=True)
  compensation_mode = models.TextField(blank=True, null=True)
  exemption_from_obligation_to_compensate = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿期间-table
class performance_forecast_compensation_compensation_period(models.Model):
  class Meta:
    db_table = "performance_forecast_compensation_compensation_period"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  each_year_performance_commitment_period_flag = models.BooleanField(blank=False, null=False, default=False)
  performance_commitment_year_flag = models.BooleanField(blank=False, null=False, default=False)
  after_cumulative_performance_commitment_period_expires_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿金额-table
class performance_forecast_compensation_compensation_amount(models.Model):
  class Meta:
    db_table = "performance_forecast_compensation_compensation_amount"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  balance_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  premium_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_indicators_types = models.TextField(blank=True, null=True)
  compensation_calculation_formula = models.TextField(blank=True, null=True)
  compensation_upper_limit = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-form
class commitment_net_profit_operational_cash_flow_contract_amount(models.Model):
  class Meta:
    db_table = "commitment_net_profit_operational_cash_flow_contract_amount"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  row_id = models.AutoField(primary_key=True)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  share_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  share_or_cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  other_assets_recognized_by_listed_companies_compensation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-股份补偿-form
class operational_cash_flow_contract_amount_share_compensation(models.Model):
  class Meta:
    db_table = "operational_cash_flow_contract_amount_share_compensation"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  share_compensation_trigger_condition = models.TextField(blank=True, null=True)
  share_compensation_upper_limit = models.TextField(blank=True, null=True)
  in_target_company_compensation_according_to_proportion_flag = models.BooleanField(blank=False, null=False, default=False)
  in_proportion_to_shareholding_in_listed_companies_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  joint_several_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  supplementary_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  share_quantity_calculating_method_should_be_compensated = models.TextField(blank=True, null=True)
  share_quantity_adjustment_should_be_compensated = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-现金补偿-form
class profit_operational_cash_flow_contract_amount_cash_compensation(models.Model):
  class Meta:
    db_table = "profit_operational_cash_flow_contract_amount_cash_compensation"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  cash_compensation_trigger_conditions = models.TextField(blank=True, null=True)
  cash_compensation_ceiling = models.TextField(blank=True, null=True)
  in_target_company_compensation_according_to_proportion_flag = models.BooleanField(blank=False, null=False, default=False)
  in_proportion_to_shareholding_in_listed_companies_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  joint_several_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  supplementary_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  calculating_amount_of_compensable_cash_method = models.TextField(blank=True, null=True)
  compensable_cash_amount_adjustment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-承诺存货-form
class forecast_compensation_compensation_mode_committed_inventory(models.Model):
  class Meta:
    db_table = "forecast_compensation_compensation_mode_committed_inventory"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_trigger_conditions = models.TextField(blank=True, null=True)
  cash_compensation_ceiling = models.TextField(blank=True, null=True)
  in_target_company_compensation_according_to_proportion_flag = models.BooleanField(blank=False, null=False, default=False)
  in_proportion_to_shareholding_in_listed_companies_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  joint_several_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  supplementary_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  calculating_amount_of_compensable_cash_method = models.TextField(blank=True, null=True)
  compensable_cash_amount_adjustment = models.TextField(blank=True, null=True)
  other_assets_recognized_by_listed_companies_compensation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-应收账款-form
class forecast_compensation_compensation_mode_accounts_receivable(models.Model):
  class Meta:
    db_table = "forecast_compensation_compensation_mode_accounts_receivable"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_trigger_conditions = models.TextField(blank=True, null=True)
  cash_compensation_ceiling = models.TextField(blank=True, null=True)
  in_target_company_compensation_according_to_proportion_flag = models.BooleanField(blank=False, null=False, default=False)
  in_proportion_to_shareholding_in_listed_companies_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  joint_several_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  supplementary_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  calculating_amount_of_compensable_cash_method = models.TextField(blank=True, null=True)
  compensable_cash_amount_adjustment = models.TextField(blank=True, null=True)
  other_assets_recognized_by_listed_companies_compensation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿方式-长期应收款-form
class forecast_compensation_compensation_mode_long_term_receivables(models.Model):
  class Meta:
    db_table = "forecast_compensation_compensation_mode_long_term_receivables"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_trigger_conditions = models.TextField(blank=True, null=True)
  cash_compensation_ceiling = models.TextField(blank=True, null=True)
  in_target_company_compensation_according_to_proportion_flag = models.BooleanField(blank=False, null=False, default=False)
  in_proportion_to_shareholding_in_listed_companies_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  joint_several_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  supplementary_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  calculating_amount_of_compensable_cash_method = models.TextField(blank=True, null=True)
  compensable_cash_amount_adjustment = models.TextField(blank=True, null=True)
  other_assets_recognized_by_listed_companies_compensation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-table
class performance_forecast_compensation_compensation_implementation(models.Model):
  class Meta:
    db_table = "performance_forecast_compensation_compensation_implementation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  commitment_to_net_profit_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_net_operating_cash_flow_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_sign_contract_amount_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_accounts_receivable_flag = models.BooleanField(blank=False, null=False, default=False)
  committed_inventory_flag = models.BooleanField(blank=False, null=False, default=False)
  commitment_to_long_term_receivables_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-股份补偿-table
class to_net_profit_contract_amount_amount_share_compensation(models.Model):
  class Meta:
    db_table = "to_net_profit_contract_amount_amount_share_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  share_repurchase_cancellation_flag = models.BooleanField(blank=False, null=False, default=False)
  charge_share_transfer_free_flag = models.BooleanField(blank=False, null=False, default=False)
  share_presentation_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-现金补偿-table
class to_net_profit_contract_amount_amount_cash_compensation(models.Model):
  class Meta:
    db_table = "to_net_profit_contract_amount_amount_cash_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  direct_cash_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_special_account_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-承诺存货-现金补偿-table
class implementation_committed_inventory_cash_compensation(models.Model):
  class Meta:
    db_table = "implementation_committed_inventory_cash_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  direct_cash_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_special_account_flag = models.BooleanField(blank=False, null=False, default=False)
  bond_flag = models.BooleanField(blank=False, null=False, default=False)
  other_assets_payment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-应收账款-现金补偿-table
class implementation_accounts_receivable_cash_compensation(models.Model):
  class Meta:
    db_table = "implementation_accounts_receivable_cash_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  direct_cash_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_special_account_flag = models.BooleanField(blank=False, null=False, default=False)
  bond_flag = models.BooleanField(blank=False, null=False, default=False)
  other_assets_payment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿-补偿实施-长期应收款-现金补偿-table
class implementation_long_term_receivables_cash_compensation(models.Model):
  class Meta:
    db_table = "implementation_long_term_receivables_cash_compensation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  direct_cash_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_special_account_flag = models.BooleanField(blank=False, null=False, default=False)
  bond_flag = models.BooleanField(blank=False, null=False, default=False)
  other_assets_payment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测补偿担保-form
class performance_forecast_compensation_guarantee(models.Model):
  class Meta:
    db_table = "performance_forecast_compensation_guarantee"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  guarantee = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  guarantee_mode_share_pledge_guarantee_flag = models.BooleanField(blank=False, null=False, default=False)
  guarantee_mode_margin_guarantee_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测担保-担保方式-股份质押担保-form
class forecast_guarantee_guarantee_mode_share_pledge_guarantee(models.Model):
  class Meta:
    db_table = "forecast_guarantee_guarantee_mode_share_pledge_guarantee"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  pledgor = models.TextField(blank=True, null=True)
  pledge_subject = models.TextField(blank=True, null=True)
  pledge_subject_matter = models.TextField(blank=True, null=True)
  pledge_subject_computation_method = models.TextField(blank=True, null=True)
  pledgee = models.TextField(blank=True, null=True)
  pledge_period = models.TextField(blank=True, null=True)
  profits_during_pledge_period_distribution = models.TextField(blank=True, null=True)
  pledge_lifting_relieving_conditions = models.TextField(blank=True, null=True)
  pledge_lifting_relief_ratio = models.TextField(blank=True, null=True)
  pledge_lifting_relieving_formalities = models.TextField(blank=True, null=True)
  pledge_lifting_removable_share_quantity_adjustment = models.TextField(blank=True, null=True)
  can_be_pledged_again_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩预测担保-担保方式-保证金担保-form
class performance_forecast_guarantee_guarantee_mode_margin_guarantee(models.Model):
  class Meta:
    db_table = "performance_forecast_guarantee_guarantee_mode_margin_guarantee"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  guarantor = models.TextField(blank=True, null=True)
  margin_guarantee_object = models.TextField(blank=True, null=True)
  margin_payment_method_cash = models.TextField(blank=True, null=True)
  margin_payment_method_share_pledge = models.TextField(blank=True, null=True)
  margin_calculation_method_cash = models.TextField(blank=True, null=True)
  margin_calculation_method_share_pledge = models.TextField(blank=True, null=True)
  margin_account_management = models.TextField(blank=True, null=True)
  guaranty_period = models.TextField(blank=True, null=True)
  profit_distribution_during_guarantee_period = models.TextField(blank=True, null=True)
  margin_return_restitution_conditions = models.TextField(blank=True, null=True)
  margin_return_restitution_amount = models.TextField(blank=True, null=True)
  margin_return_restitution_procedures = models.TextField(blank=True, null=True)
  margin_return_return_amount_adjustment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 业绩承诺完成情况-form
class performance_commitment_completion(models.Model):
  class Meta:
    db_table = "performance_commitment_completion"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  committed_person = models.TextField(blank=True, null=True)
  identity = models.TextField(blank=True, null=True)
  stock_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  year = models.TextField(blank=True, null=True)
  actual_performance_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  performance_commitment_amount = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  difference = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  completion_rate = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试时间-table
class impairment_test_time(models.Model):
  class Meta:
    db_table = "impairment_test_time"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  profit_commitment_period_expiration = models.TextField(blank=True, null=True)
  each_fiscal_year_end = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试流程-table
class impairment_test_flow(models.Model):
  class Meta:
    db_table = "impairment_test_flow"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  how_to_determine_accounting_firms = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿条件-table
class impairment_test_compensation_conditions(models.Model):
  class Meta:
    db_table = "impairment_test_compensation_conditions"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  during_profit_commitment_period_final_impairment_flag = models.BooleanField(blank=False, null=False, default=False)
  items_to_be_deducted_from_impairment = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿金额-form
class testing_compensation_arrangement_compensation_amount(models.Model):
  class Meta:
    db_table = "testing_compensation_arrangement_compensation_amount"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  compensatory_obligor_status = models.TextField(blank=True, null=True)
  compensation_amount_calculation_formula = models.TextField(blank=True, null=True)
  compensation_amount_upper_limit = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-form
class impairment_testing_compensation_arrangement_compensation_mode(models.Model):
  class Meta:
    db_table = "impairment_testing_compensation_arrangement_compensation_mode"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  compensatory_obligor_status = models.TextField(blank=True, null=True)
  share_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  share_compensation_priority_flag = models.BooleanField(blank=False, null=False, default=False)
  share_compensation_trigger_condition = models.TextField(blank=True, null=True)
  cash_compensation_priority_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_trigger_conditions = models.TextField(blank=True, null=True)
  compensation_compensation_in_proportion_to_shareholding = models.TextField(blank=True, null=True)
  compensation_compensation_in_other_proportions = models.TextField(blank=True, null=True)
  compensation_share_number_calculating_method = models.TextField(blank=True, null=True)
  calculating_amount_of_compensatory_cash_method = models.TextField(blank=True, null=True)
  cash_compensation_proportional_commitment_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_each_party_undertakes_how_to_calculate_amount = models.TextField(blank=True, null=True)
  cash_dividend_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_dividend_calculation_period = models.TextField(blank=True, null=True)
  compensation_obligation_joint_several_liability_flag = models.BooleanField(blank=False, null=False, default=False)
  compensation_implementation_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-减值补偿股份数量调整-form
class mode_impairment_compensation_share_quantity_adjustment(models.Model):
  class Meta:
    db_table = "mode_impairment_compensation_share_quantity_adjustment"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  adjustment_situation = models.TextField(blank=True, null=True)
  adjust_calculation_formula = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-股份补偿实施-form
class compensation_mode_share_compensation_implementation(models.Model):
  class Meta:
    db_table = "compensation_mode_share_compensation_implementation"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  compensatory_obligor_status = models.TextField(blank=True, null=True)
  share_compensation_operation_arrangement = models.TextField(blank=True, null=True)
  companies_share_repurchase_write_off_scheme_review_process = models.TextField(blank=True, null=True)
  compensation_obligator_share_transfer = models.TextField(blank=True, null=True)
  share_cancellation = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-现金补偿实施-form
class arrangement_compensation_mode_cash_compensation_implementation(models.Model):
  class Meta:
    db_table = "arrangement_compensation_mode_cash_compensation_implementation"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  compensatory_obligor_status = models.TextField(blank=True, null=True)
  direct_cash_compensation_flag = models.BooleanField(blank=False, null=False, default=False)
  cash_compensation_opening_special_account_flag = models.BooleanField(blank=False, null=False, default=False)
  agreements_with_listed_companies_commercial_banks_flag = models.BooleanField(blank=False, null=False, default=False)
  companies_to_determine_amount_impairment_compensation_time = models.TextField(blank=True, null=True)
  process_determining_amount_of_impairment_compensation = models.TextField(blank=True, null=True)
  performance_compensation_obligation_time_limit = models.TextField(blank=True, null=True)
  performing_compensation_obligation_way = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-现金补偿实施-现金补偿专用账户-form
class compensation_implementation_cash_compensation_special_account(models.Model):
  class Meta:
    db_table = "compensation_implementation_cash_compensation_special_account"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  compensatory_obligor = models.TextField(blank=True, null=True)
  compensatory_obligor_status = models.TextField(blank=True, null=True)
  attention_of_listed_companies_duty = models.TextField(blank=True, null=True)
  funs_restrictions_on_use = models.TextField(blank=True, null=True)
  funs_rights_restriction = models.TextField(blank=True, null=True)
  funs_transition_condition = models.TextField(blank=True, null=True)
  funs_roll_out_restriction = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 减值测试补偿安排-补偿方式-现金补偿实施-现金补偿专用账户-专用账户内资金转出比例限制-table
class special_account_special_funs_outbound_proportional_limitation(models.Model):
  class Meta:
    db_table = "special_account_special_funs_outbound_proportional_limitation"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  first_year = models.TextField(blank=True, null=True)
  first_year_transfer_ratio_limit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  second_years = models.TextField(blank=True, null=True)
  transfer_proportion_limitation_in_second_year = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  third_year = models.TextField(blank=True, null=True)
  third_year_transfer_ratio_limit = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 奖励期间-table
class reward_period(models.Model):
  class Meta:
    db_table = "reward_period"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  earnings_commitment_period_flag = models.BooleanField(blank=False, null=False, default=False)
  first_year = models.TextField(blank=True, null=True)
  second_years = models.TextField(blank=True, null=True)
  third_year = models.TextField(blank=True, null=True)
  fourth_years = models.TextField(blank=True, null=True)
  fifth_years = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 触发条件-table
class trigger_condition(models.Model):
  class Meta:
    db_table = "trigger_condition"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  performance_commitment_completed_in_each_year_flag = models.BooleanField(blank=False, null=False, default=False)
  accumulated_net_profit_excess_flag = models.BooleanField(blank=False, null=False, default=False)
  accumulated_net_profit_excess_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  operating_cash_flow_net_excess_flag = models.BooleanField(blank=False, null=False, default=False)
  operating_cash_flow_net_excess_ratio = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)
  contract_signed_excess_amount_flag = models.BooleanField(blank=False, null=False, default=False)
  contract_amount_excess_proportion = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=2)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 考核指标-form
class assessment_index(models.Model):
  class Meta:
    db_table = "assessment_index"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  assessment_indicators_types = models.TextField(blank=True, null=True)
  evaluation_indicator_calculation_formula = models.TextField(blank=True, null=True)
  deduction_items_type = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 奖励金额-form
class reward_amount(models.Model):
  class Meta:
    db_table = "reward_amount"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  amount_upper_limit = models.TextField(blank=True, null=True)
  cumulative_calculation_flag = models.BooleanField(blank=False, null=False, default=False)
  cumulative_calculation_formula = models.TextField(blank=True, null=True)
  stage_calculation_flag = models.BooleanField(blank=False, null=False, default=False)
  phase_i_calculation_formula = models.TextField(blank=True, null=True)
  phase_ii_calculation_formula = models.TextField(blank=True, null=True)
  phase_iii_calculation_formula = models.TextField(blank=True, null=True)
  not_calculated_according_to_excess_range_flag = models.BooleanField(blank=False, null=False, default=False)
  do_not_calculate_formula_according_to_excess_range_flag = models.BooleanField(blank=False, null=False, default=False)
  calculated_by_excess_range_in_segments_flag = models.BooleanField(blank=False, null=False, default=False)
  paragraph_one_excess_range = models.TextField(blank=True, null=True)
  paragraph_one_incentive_amount = models.TextField(blank=True, null=True)
  paragraph_two_excess_range = models.TextField(blank=True, null=True)
  paragraph_two_incentive_amount = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 支付安排-form
class payment_arrangements(models.Model):
  class Meta:
    db_table = "payment_arrangements"

  row_id = models.AutoField(primary_key=True)
  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  payment_body = models.TextField(blank=True, null=True)
  reward_object_name = models.TextField(blank=True, null=True)
  reward_object_identity = models.TextField(blank=True, null=True)
  one_time_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  installment_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  installment_payment_arrangement = models.TextField(blank=True, null=True)
  cash_payment_flag = models.BooleanField(blank=False, null=False, default=False)
  other_payments = models.TextField(blank=True, null=True)
  payment_time = models.TextField(blank=True, null=True)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return


# 账务处理-table
class accounting_treatment(models.Model):
  class Meta:
    db_table = "accounting_treatment"

  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)
  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)
  row_id = models.AutoField(primary_key=True)
  reward_not_deducted_from_net_profit_realized_amount_flag = models.BooleanField(blank=False, null=False, default=False)
  net_profit_not_affected_actual_accounting_treatment_flag = models.BooleanField(blank=False, null=False, default=False)
  incentive_amount_deducted_from_personal_income_tax_flag = models.BooleanField(blank=False, null=False, default=False)

  def get_attr(self, attr_name):
    return getattr(self, attr_name)

  def set_attr(self, attr_name, content):
    setattr(self, attr_name, content)
    return
