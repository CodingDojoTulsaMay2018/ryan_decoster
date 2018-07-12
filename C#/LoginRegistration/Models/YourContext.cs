using Microsoft.EntityFrameworkCore;

namespace LoginRegistration.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) {}
        public DbSet<User> Users { get; set; } 
    }
}