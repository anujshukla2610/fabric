CREATE TABLE [dbo].[gold_monthly_summary] (

	[year_month] varchar(8) NULL, 
	[region] varchar(50) NULL, 
	[total_revenue] decimal(38,2) NULL, 
	[total_orders] int NULL, 
	[avg_order_value] decimal(38,6) NULL, 
	[revenue_rank_in_month] bigint NULL
);