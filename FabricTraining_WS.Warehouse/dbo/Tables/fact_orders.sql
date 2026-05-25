CREATE TABLE [dbo].[fact_orders] (

	[order_id] int NULL, 
	[customer_id] int NULL, 
	[product_id] int NULL, 
	[order_date] date NULL, 
	[quantity] int NULL, 
	[total_amount] decimal(10,2) NULL
);