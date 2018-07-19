using Microsoft.EntityFrameworkCore;

namespace ProductsCategories.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) {}
        public DbSet<Product> Products { get; set; }
        public DbSet<Category> Categories { get; set; }
        public DbSet<Grouping> Categories_Products { get; set; }
    }
}