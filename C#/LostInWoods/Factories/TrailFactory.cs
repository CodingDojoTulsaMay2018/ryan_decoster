using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
using LostInWoods.Models;
using Microsoft.Extensions.Options;
 
namespace LostInWoods.Factory
{
    public class TrailFactory : IFactory<Trail>
    {
        private MySqlOptions _options;
        public TrailFactory(IOptions<MySqlOptions> config)
        {
            _options = config.Value;
        }

        internal IDbConnection Connection
        {
            get {
                return new MySqlConnection(_options.ConnectionString);
            }
        }
        public void Add(Trail newTrail)
        {
            using (IDbConnection dbConnection = Connection) {
                string query = "INSERT INTO trails (name, description, length, gain, longitude, latitude) VALUES (@Name, @Description, @Length, @Gain, @Longitude, @Latitude)";
                dbConnection.Open();
                dbConnection.Execute(query, newTrail);
            }
        }
        public IEnumerable<Trail> ShowAll()
        {
            using (IDbConnection dbConnection = Connection)
            {
                dbConnection.Open();
                return dbConnection.Query<Trail>("SELECT * FROM trails");
            }
        }
        public Trail FindByID(int id)
        {
            using (IDbConnection dbConnection = Connection)
            {
                System.Console.WriteLine(id);
                dbConnection.Open();
                return dbConnection.Query<Trail>("SELECT * FROM trails WHERE id = @Id", new { Id = id}).FirstOrDefault();
            }
        }
    }
}