using System.ComponentModel.DataAnnotations;
namespace LostInWoods.Models
{
    public abstract class BaseEntity {}
    public class Trail : BaseEntity
    {
        [Key]
        public long Id { get; set; }
 
        [Required]
        [MinLength(5)]
        [MaxLength(140)]
        public string Name { get; set; }
 
        [Required]
        [MinLength(10)]
        public string Description { get; set; }
 
        [Required]
        public double Length { get; set; }

        [Required]
        public int Gain { get; set; }

        [Required]
        public double Longitude { get; set; }

        [Required]
        public double Latitude { get; set; }
    }
}
